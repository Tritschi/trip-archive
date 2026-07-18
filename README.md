# Trip Archive

> Archive journeys permanently from Home Assistant Recorder and display them on an interactive map.

## Current release

**v0.3.0-beta.1**

This is the first beta release of Trip Archive for Home Assistant. The complete Recorder-to-archive workflow is available and the dashboard has reached its Beta 1 UI freeze.

## Features

- Generate trips directly from Home Assistant Recorder
- Select the trip time range and source entities in the archive dialog
- Store immutable raw GPS and optional distance-counter data
- Rebuild statistics and simplified display routes from archived raw data
- Browse saved trips in the Home Assistant sidebar panel
- View trips on a responsive, interactive map
- Show total distance, original GPS points, display points and segments
- Safely delete trips from the trip detail view with confirmation
- Use the dashboard in desktop browsers and the Home Assistant companion app

Trip Archive intentionally has no file, JSON, GPX, Garmin or OwnTracks importer. Trips are generated from Home Assistant Recorder only.

## Reference validation

The Scotland 2026 reference trip was successfully recreated from Recorder with these values:

- Start distance counter: **22,334 km**
- End distance counter: **26,789 km**
- Total distance: **4,455 km**
- Original GPS points: **21,984**
- Display points: **1,869**

## Installation

1. Download the install ZIP attached to the GitHub release.
2. Extract it.
3. Replace the existing integration folder:

```text
/config/custom_components/trip_archive/
```

4. Restart Home Assistant completely.
5. Reload the browser or companion app frontend if an older panel version is still cached.

Do not replace or delete the archived trip data folder:

```text
/config/trip_archive/
```

The sidebar panel registers itself. No `panel_custom` YAML entry is required.

## Storage and safety

Recorder history is read only. Trip Archive does not modify or purge Recorder data.

Archived data is stored separately under `/config/trip_archive/`. Raw source data remains immutable. Statistics, simplified routes and other derived files can be regenerated.

## Beta status

This is a beta release. Back up the Home Assistant configuration and `/config/trip_archive/` before updating.

The next major development focus is automatic intelligent segment and stage detection. The Beta 1 dashboard design is considered frozen except for actual display defects.

## Documentation

- [Architecture](docs/architecture.md)
- [Storage layout](docs/storage.md)
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)
- [Contributing](CONTRIBUTING.md)
- [Release checklist](RELEASE_CHECKLIST.md)

## License

MIT
