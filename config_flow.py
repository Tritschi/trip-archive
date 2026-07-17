"""Config flow for Trip Archive."""
from __future__ import annotations
from typing import Any
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult
from .const import CONF_STORAGE_PATH, DEFAULT_STORAGE_PATH, DOMAIN

class TripArchiveConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle Trip Archive setup."""
    VERSION = 1

    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult:
        """Create the local Trip Archive instance."""
        if self._async_current_entries():
            return self.async_abort(reason="already_configured")
        if user_input is not None:
            storage_path = user_input[CONF_STORAGE_PATH].strip().strip("/")
            if not storage_path or ".." in storage_path.split("/"):
                return self.async_show_form(
                    step_id="user",
                    data_schema=self._schema(user_input[CONF_STORAGE_PATH]),
                    errors={CONF_STORAGE_PATH: "invalid_storage_path"},
                )
            return self.async_create_entry(
                title="Trip Archive",
                data={CONF_STORAGE_PATH: storage_path},
            )
        return self.async_show_form(step_id="user", data_schema=self._schema())

    @staticmethod
    def _schema(default: str = DEFAULT_STORAGE_PATH) -> vol.Schema:
        return vol.Schema({vol.Required(CONF_STORAGE_PATH, default=default): str})
