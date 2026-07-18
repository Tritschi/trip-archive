"""Constants for Trip Archive."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Final

DOMAIN: Final = "trip_archive"
NAME: Final = "Trip Archive"

# Home Assistant requires the integration version in manifest.json. Reading it
# here keeps manifest.json as the single maintained source of the release version.
_MANIFEST = json.loads((Path(__file__).with_name("manifest.json")).read_text(encoding="utf-8"))
VERSION: Final[str] = _MANIFEST["version"]

CONF_STORAGE_PATH: Final = "storage_path"
DEFAULT_STORAGE_PATH: Final = "trip_archive"
DATA_STORAGE_MANAGER: Final = "storage_manager"
DATA_WEBSOCKET_REGISTERED: Final = "websocket_registered"
SCHEMA_VERSION: Final = 1
DERIVED_GENERATOR_VERSION: Final = VERSION

SERVICE_CREATE_TRIP: Final = "create_trip"
SIGNAL_TRIPS_UPDATED: Final = f"{DOMAIN}_trips_updated"
