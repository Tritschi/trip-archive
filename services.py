"""Home Assistant actions for Trip Archive."""
from __future__ import annotations

from functools import partial

import voluptuous as vol

from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.dispatcher import async_dispatcher_send

from .const import DATA_STORAGE_MANAGER, DOMAIN, SERVICE_CREATE_TRIP, SIGNAL_TRIPS_UPDATED
from .models import TripMetadata, slugify_trip_id
from .recorder.archive import async_read_trip_sources, iso_utc

ACTIVITY_TYPES = ["vehicle_trip", "hike", "bike", "walk", "other"]

CREATE_TRIP_SCHEMA = vol.Schema({
    vol.Required("name"): cv.string,
    vol.Required("start"): cv.datetime,
    vol.Required("end"): cv.datetime,
    vol.Required("tracker_entity"): cv.entity_id,
    vol.Required("odometer_entity"): cv.entity_id,
    vol.Optional("activity_type", default="vehicle_trip"): vol.In(ACTIVITY_TYPES),
    vol.Optional("tags", default=[]): vol.All(cv.ensure_list, [cv.string]),
    vol.Optional("tolerance_m", default=35.0): vol.All(vol.Coerce(float), vol.Range(min=0, max=2000)),
    vol.Optional("gap_minutes", default=360): vol.All(vol.Coerce(int), vol.Range(min=0, max=10080)),
})


def _storage_manager(hass: HomeAssistant):
    domain_data = hass.data.get(DOMAIN, {})
    for value in domain_data.values():
        if isinstance(value, dict) and DATA_STORAGE_MANAGER in value:
            return value[DATA_STORAGE_MANAGER]
    raise RuntimeError("Trip Archive is not configured")


async def async_register_services(hass: HomeAssistant) -> None:
    if hass.services.has_service(DOMAIN, SERVICE_CREATE_TRIP):
        return

    async def async_create_trip(call: ServiceCall) -> None:
        start, end = call.data["start"], call.data["end"]
        if end <= start:
            raise ValueError("Trip end must be later than trip start")
        gps, odometer, unit = await async_read_trip_sources(hass, start, end, call.data["tracker_entity"], call.data["odometer_entity"])
        if len(gps) < 2:
            raise ValueError("Recorder contains fewer than two GPS points in this period")
        manager = _storage_manager(hass)
        base_id = slugify_trip_id(call.data["name"], iso_utc(start))
        trip_id = await hass.async_add_executor_job(manager.unique_trip_id, base_id)
        metadata = TripMetadata(id=trip_id, name=call.data["name"], activity_type=call.data["activity_type"], start=iso_utc(start), end=iso_utc(end), tags=list(call.data["tags"]))
        sources = {"created_by": "home_assistant_recorder", "tracker_entity": call.data["tracker_entity"], "odometer_entity": call.data["odometer_entity"], "recorder_start": iso_utc(start), "recorder_end": iso_utc(end)}
        await hass.async_add_executor_job(partial(manager.create_trip, metadata, sources, gps, odometer, gps_source_entity=call.data["tracker_entity"], odometer_source_entity=call.data["odometer_entity"], odometer_unit=unit or "km", tolerance_m=call.data["tolerance_m"], gap_minutes=call.data["gap_minutes"]))
        async_dispatcher_send(hass, SIGNAL_TRIPS_UPDATED)

    hass.services.async_register(DOMAIN, SERVICE_CREATE_TRIP, async_create_trip, schema=CREATE_TRIP_SCHEMA)


async def async_unregister_services(hass: HomeAssistant) -> None:
    if hass.services.has_service(DOMAIN, SERVICE_CREATE_TRIP):
        hass.services.async_remove(DOMAIN, SERVICE_CREATE_TRIP)
