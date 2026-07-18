# Trip Archive

> Permanently archive journeys from Home Assistant Recorder and explore them on an interactive map.

Trip Archive is a custom Home Assistant integration for preserving historical GPS and odometer data before Recorder purges it. Raw source data remains immutable; maps, statistics and simplified routes are derived data that can be rebuilt at any time.

## Current test version

**v0.3.0-alpha.4.4**

This version provides the first complete Recorder-to-map workflow:

1. select a trip name, time range, device tracker and odometer entity,
2. read GPS and odometer history directly from Home Assistant Recorder,
3. store the original samples permanently below `/config/trip_archive/`,
4. generate rebuildable statistics and a simplified display route,
5. select archived trips in the Trip Archive sidebar panel,
6. inspect the route on a large, zoomable map in browser or Companion App.

The panel includes:

- a compact list of archived trips,
- a large interactive map,
- start and destination markers,
- automatic route fitting and **Auf Route zoomen**,
- trip distance, odometer values and GPS point counts,
- a Recorder archive dialog,
- Home Assistant navigation with a hamburger menu in browser and app.

## Recorder only

Trip Archive intentionally has no JSON, GPX, Garmin, OwnTracks or other file importer. Archived trips are generated from the Home Assistant installation itself. The Recorder database is read only and is never modified or purged by Trip Archive.

## Installation

Download the install package and replace:

```text
/config/custom_components/trip_archive/
```

with the included `trip_archive` folder. Restart Home Assistant afterwards.

Do **not** replace or delete the permanent data directory:

```text
/config/trip_archive/
```

The sidebar panel is registered automatically by the integration. No `panel_custom` entry in `configuration.yaml` is required.

## Storage principle

```text
/config/trip_archive/
└── trips/
    └── <trip-id>/
        ├── trip.json
        ├── sources.json
        ├── raw/
        │   ├── gps.json
        │   └── odometer.json
        └── derived/
            ├── statistics.json
            └── route_display.json
```

Files below `raw/` are the permanent source archive. Files below `derived/` can be regenerated from those originals.

## Verified reference trip

The Scotland 2026 trip was regenerated directly from Home Assistant Recorder and reproduced the reference values:

- 22,334 km start odometer
- 26,789 km end odometer
- 4,455 km difference
- 21,984 original GPS points
- 1,869 simplified display points

## Project status

Trip Archive is alpha software. Back up `/config/trip_archive/` before testing new versions. Tested versions are tagged in the repository.

## License

MIT
