## 0.3.0-alpha.3.4

- tolerate incomplete archived trips with missing derived files
- allow incomplete trips to be opened and deleted without WebSocket errors
- locate trip ownership by directory existence rather than loading derived data
- load Leaflet CSS inside the panel Shadow DOM
- show elapsed Recorder archive time and suppress conflicting refreshes while creating

# Changelog


## 0.3.0-alpha.3.3

- Trip list now falls back to the `sensor.trip_archive_trips` attributes and merges them with WebSocket results.
- Disabled long-term caching for the panel static path.
- Added a version query parameter to the panel module URL to force frontend refreshes after upgrades.

## 0.3.0-alpha.3.1

- Fixed an inconsistent panel state where the summary sensor showed archived trips but the sidebar panel listed none.
- WebSocket commands now resolve the storage manager deterministically and can recover from duplicate legacy config entries.
- Trip listing merges and de-duplicates trips across all configured managers.

## 0.3.0-alpha.3

- Restored the Trip Archive sidebar dashboard based on the proven 0.2.0 panel.
- Panel is registered by the integration; no `panel_custom` YAML is required.
- Added trip list, large zoomable map, statistics and archive dialog.
- Added Recorder-only generation for GPS and odometer source data.
- Stores immutable raw data in the 0.3 trip directory structure.
- Added route gap segmentation, derived regeneration and trip deletion.
- No file, GPX or JSON import support.
