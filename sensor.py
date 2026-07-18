"""Sensor entities for Trip Archive."""

from __future__ import annotations

from typing import Any

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import (
    DATA_STORAGE_MANAGER,
    DOMAIN,
    NAME,
    SIGNAL_TRIPS_UPDATED,
    VERSION,
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Trip Archive summary sensor."""
    manager = hass.data[DOMAIN][entry.entry_id][DATA_STORAGE_MANAGER]
    async_add_entities(
        [TripArchiveSummarySensor(hass, entry, manager)],
        update_before_add=True,
    )


class TripArchiveSummarySensor(SensorEntity):
    """Show the archive size and readable trip summaries."""

    _attr_has_entity_name = True
    _attr_name = "Trips"
    _attr_icon = "mdi:map-marker-path"

    def __init__(self, hass, entry, manager) -> None:
        """Initialize the summary sensor."""
        self.hass = hass
        self._entry = entry
        self._manager = manager
        self._trips: list[dict[str, Any]] = []
        self._attr_unique_id = f"{entry.entry_id}_trips"

    @property
    def native_value(self) -> int:
        """Return the number of archived trips."""
        return len(self._trips)

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return compact trip summaries as attributes."""
        latest = self._trips[0] if self._trips else None
        return {
            "version": VERSION,
            "storage_path": str(self._manager.root),
            "latest_trip": latest,
            "trips": self._trips,
        }

    @property
    def device_info(self) -> dict[str, Any]:
        """Group the sensor under a Trip Archive service device."""
        return {
            "identifiers": {(DOMAIN, self._entry.entry_id)},
            "name": NAME,
            "manufacturer": "Trip Archive",
            "model": "Local journey archive",
            "sw_version": VERSION,
        }

    async def async_update(self) -> None:
        """Read the current archive index."""
        self._trips = await self.hass.async_add_executor_job(
            self._manager.list_trips
        )

    async def async_added_to_hass(self) -> None:
        """Listen for trip creation and refresh immediately."""
        await super().async_added_to_hass()

        @callback
        def _handle_trips_updated() -> None:
            self.async_schedule_update_ha_state(force_refresh=True)

        self.async_on_remove(
            async_dispatcher_connect(
                self.hass,
                SIGNAL_TRIPS_UPDATED,
                _handle_trips_updated,
            )
        )
