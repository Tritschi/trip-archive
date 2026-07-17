# Trip Archive

> Archive your journeys permanently in Home Assistant.

## Current test version

**v0.3.0-alpha.2.1**

This version completes the first storage round trip:

1. create a trip,
2. save it permanently,
3. read it back into Home Assistant.

Trip Archive now creates a sensor named similar to:

```text
sensor.trip_archive_trips
```

Its state is the number of archived trips. Its attributes contain the latest
trip and a compact list of all trips.

Recorder import and the route map are not included yet.

## Installation

Replace:

```text
/config/custom_components/trip_archive/
```

with the `trip_archive` folder from the install package, then restart Home
Assistant. The existing integration and archive data remain in place.

## Test

Open **Developer tools → States** and search for:

```text
trip_archive
```

The Trips sensor should show the number `1` when the Alpha 2 test trip exists.
Open the attributes to inspect its name, period, activity type and statistics.

Create another trip with `trip_archive.create_trip`. The sensor should update
without a restart.

## Safety

This alpha only reads Trip Archive's own JSON files. It does not query,
modify or purge Home Assistant Recorder history.

## License

MIT
