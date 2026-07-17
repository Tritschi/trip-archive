"""Trip Archive integration."""
from __future__ import annotations
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import CONF_STORAGE_PATH, DATA_STORAGE_MANAGER, DATA_WEBSOCKET_REGISTERED, DEFAULT_STORAGE_PATH, DOMAIN
from .storage.manager import TripStorageManager
from .websocket import async_register_websocket_commands
_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Trip Archive from a config entry."""
    relative_path = entry.data.get(CONF_STORAGE_PATH, DEFAULT_STORAGE_PATH)
    root = hass.config.path(relative_path)
    manager = TripStorageManager(root)
    await hass.async_add_executor_job(manager.initialize)
    domain_data = hass.data.setdefault(DOMAIN, {})
    domain_data[entry.entry_id] = {DATA_STORAGE_MANAGER: manager}
    if not domain_data.get(DATA_WEBSOCKET_REGISTERED):
        async_register_websocket_commands(hass)
        domain_data[DATA_WEBSOCKET_REGISTERED] = True
    _LOGGER.info("Trip Archive initialized at %s", root)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a Trip Archive config entry."""
    domain_data = hass.data.get(DOMAIN, {})
    domain_data.pop(entry.entry_id, None)
    return True
