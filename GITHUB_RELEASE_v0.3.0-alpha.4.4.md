# Trip Archive v0.3.0-alpha.4.4

This release completes the first usable Recorder-to-map workflow.

## Highlights

- Archive GPS and odometer history directly from Home Assistant Recorder.
- Keep immutable raw data permanently below `/config/trip_archive/`.
- Browse archived trips in a dedicated Home Assistant sidebar dashboard.
- Display routes on a large interactive map with start and destination markers.
- Use the Home Assistant hamburger menu in both browser and Companion App.
- No external file importer: Home Assistant Recorder remains the only source.

## Verified Scotland reference

The Scotland 2026 trip was regenerated from Recorder with the expected values:

- 22,334 km start
- 26,789 km end
- 4,455 km difference
- 21,984 original GPS points
- 1,869 display points

## Installation

Replace `/config/custom_components/trip_archive/` with the integration folder from the install package and restart Home Assistant.

Do not delete `/config/trip_archive/`; it contains the permanent trip archive.

This is alpha software. Back up the archive directory before upgrading.
