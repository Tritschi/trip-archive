"""Trip Archive integration."""
from __future__ import annotations

from pathlib import Path

from homeassistant.components import frontend
from homeassistant.components.http import StaticPathConfig
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import CONF_STORAGE_PATH, DATA_STORAGE_MANAGER, DEFAULT_STORAGE_PATH, DOMAIN, VERSION
from .services import async_register_services, async_unregister_services
from .storage.manager import TripStorageManager
from .websocket import async_register_websocket_commands

PLATFORMS: list[Platform] = [Platform.SENSOR]
STATIC_URL = "/trip_archive_static"
PANEL_URL = "trip-archive"
PANEL_ELEMENT = "trip-archive-panel"


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up shared commands and the sidebar dashboard."""
    frontend_dir = Path(__file__).parent / "frontend"
    await hass.http.async_register_static_paths([StaticPathConfig(STATIC_URL, str(frontend_dir), False)])
    async_register_websocket_commands(hass)

    # Register the panel from the integration itself; no configuration.yaml panel_custom entry is needed.
    frontend.async_register_built_in_panel(
        hass,
        component_name="custom",
        sidebar_title="Trip Archive",
        sidebar_icon="mdi:map-marker-path",
        frontend_url_path=PANEL_URL,
        config={"_panel_custom": {"name": PANEL_ELEMENT, "module_url": f"{STATIC_URL}/trip-archive-panel.js?v={VERSION}"}},
        require_admin=False,
        update=frontend.async_panel_exists(hass, PANEL_URL),
    )
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    relative_path = entry.options.get(CONF_STORAGE_PATH, entry.data.get(CONF_STORAGE_PATH, DEFAULT_STORAGE_PATH))
    manager = TripStorageManager(hass.config.path(relative_path))
    await hass.async_add_executor_job(manager.initialize)
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = {DATA_STORAGE_MANAGER: manager}
    await async_register_services(hass)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if not unload_ok:
        return False
    domain_data = hass.data.get(DOMAIN, {})
    domain_data.pop(entry.entry_id, None)
    configured_entries = [value for value in domain_data.values() if isinstance(value, dict) and DATA_STORAGE_MANAGER in value]
    if not configured_entries:
        await async_unregister_services(hass)
    return True
