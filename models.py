from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any
from .const import SCHEMA_VERSION

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

@dataclass(frozen=True, slots=True)
class GpsPoint:
    time: str
    lat: float
    lon: float
    accuracy: float | None = None
    def as_dict(self) -> dict[str, Any]: return asdict(self)

@dataclass(frozen=True, slots=True)
class SensorSample:
    time: str
    value: float
    def as_dict(self) -> dict[str, Any]: return asdict(self)

@dataclass(slots=True)
class TripMetadata:
    id: str
    name: str
    activity_type: str
    start: str
    end: str
    created_at: str = field(default_factory=utc_now_iso)
    updated_at: str = field(default_factory=utc_now_iso)
    status: str = "archived"
    tags: list[str] = field(default_factory=list)
    schema_version: int = SCHEMA_VERSION
    def as_dict(self) -> dict[str, Any]: return asdict(self)
