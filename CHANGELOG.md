# Changelog

## 0.3.0-alpha.4.4

- Shows the Home Assistant app bar and hamburger menu in both browser and Companion App.
- Removes the duplicate Trip Archive brand header.
- Recalculates the dashboard height so the map uses the available space below the app bar.
- Keeps the compact, map-focused dashboard layout introduced in alpha.4.x.

## 0.3.0-alpha.4.3

- Added Home Assistant navigation for narrow and app layouts.
- Restored access to the Home Assistant sidebar in Android and iOS Companion Apps.
- Updated frontend cache versioning.

## 0.3.0-alpha.4.2

- Added the native Home Assistant menu button and compact app bar.
- Preserved the desktop map-focused layout.

## 0.3.0-alpha.4.1

- Moved **Reise archivieren** into the left sidebar.
- Removed the separate page header so the trip view and map move upward.
- Replaced large statistic cards with a compact summary strip.
- Made the map consume the remaining viewport height.

## 0.3.0-alpha.4

- Added a more reliable map tile setup with fallback handling.
- Added start and destination markers.
- Added **Auf Route zoomen** and improved route fitting.
- Increased the map area and improved responsive layout behavior.

## 0.3.0-alpha.3.4

- Made incomplete legacy trip directories readable and deletable.
- Missing derived files no longer crash WebSocket requests.
- Added visible progress feedback while Recorder data is archived.
- Loaded Leaflet styles inside the panel context.

## 0.3.0-alpha.3.3

- Added a trip-list fallback from `sensor.trip_archive_trips` attributes.
- Merged sensor and WebSocket trip results.
- Disabled long-term caching for panel static assets.
- Added frontend version query parameters to force refresh after upgrades.

## 0.3.0-alpha.3.1

- Fixed an inconsistent state where the sensor contained trips but the panel listed none.
- Resolved storage managers deterministically.
- Merged and de-duplicated trips across legacy config entries.

## 0.3.0-alpha.3

- Restored the Trip Archive sidebar dashboard based on the proven 0.2.0 panel.
- Registered the panel automatically without `panel_custom` YAML.
- Added trip list, large zoomable map, statistics and archive dialog.
- Added Recorder-only generation for GPS and odometer source data.
- Stored immutable raw data in the 0.3 trip directory structure.
- Added route gap segmentation, derived regeneration and trip deletion.
- No file, GPX or JSON import support.
