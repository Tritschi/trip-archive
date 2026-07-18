# Trip Archive

> Archive journeys permanently from Home Assistant Recorder and display them on an interactive map.

## Current test version

**v0.3.0-alpha.4.3**

This alpha provides the complete first workflow:

1. select a time range and Home Assistant entities,
2. read GPS and odometer history from Recorder,
3. store immutable raw data below `/config/trip_archive/`,
4. generate statistics and a simplified display route,
5. select archived trips in the sidebar panel and inspect them on a zoomable map.

The panel includes start and destination markers, automatic route fitting, a manual “Auf Route zoomen” action, and tile-provider failover.

There is no file, JSON, GPX, Garmin, or OwnTracks import. Trip data is generated from Home Assistant Recorder only.

## Installation

Replace:

```text
/config/custom_components/trip_archive/
```

with the `trip_archive` folder from the install package, then restart Home Assistant. Do not replace or delete:

```text
/config/trip_archive/
```

The sidebar panel registers itself; no `panel_custom` entry is required.

## Safety

Recorder history is read only. Trip Archive does not modify or purge Recorder data. Raw archived trip data is kept separate from derived statistics and display routes.

## License

MIT
