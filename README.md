# Trip Archive

> Archive your journeys permanently in Home Assistant.

## Current test version

**v0.3.0-alpha.2**

Alpha 2 can:

- install through Home Assistant's integration UI
- initialize `/config/trip_archive/`
- create an empty archived trip through the `trip_archive.create_trip` action
- generate the complete trip folder structure
- maintain `index.json`
- keep raw and derived documents separated

Recorder import and the map are not included yet.

## Installation

Copy:

```text
custom_components/trip_archive/
```

to:

```text
/config/custom_components/trip_archive/
```

Restart Home Assistant, then add **Trip Archive** under
**Settings → Devices & services**.

## Alpha 2 test

Open **Developer tools → Actions**, choose:

```text
trip_archive.create_trip
```

Create a small test trip. Home Assistant should then create a folder below:

```text
/config/trip_archive/trips/
```

See `docs/alpha-2-test.md` for the exact test procedure.

## Safety

Raw source files are never recalculated or overwritten by derived processing.
This alpha does not read or change Recorder history.

## License

MIT
