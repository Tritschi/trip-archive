# Trip Archive v0.3.0-beta.1

First usable beta and the UI freeze for the initial Trip Archive dashboard.

## Highlights

- Archive journeys directly from Home Assistant Recorder.
- Preserve immutable raw GPS and distance-counter data.
- Browse archived trips in a responsive sidebar dashboard.
- Display the selected route on an interactive map.
- Use consistent coloured SVG icons for all trip statistics.
- Use a safe red outline delete action only in the trip detail view.
- Show an icon-only delete action on narrow mobile screens.
- Use clearer labels for map simplification and route-gap handling.

## Confirmed reference trip

The Scotland 2026 journey was regenerated from Home Assistant Recorder with the expected reference values:

- 4,455 km total distance
- 21,984 original GPS points
- 1,869 display points

## Important

Trip Archive reads from Home Assistant Recorder only. It does not provide JSON, GPX, Garmin, OwnTracks, or other import paths.

This is a beta pre-release. Keep a backup of `/config/trip_archive/` before upgrading.
