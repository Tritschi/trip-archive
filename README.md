# Trip Archive

Archive journeys permanently in Home Assistant before Recorder purges their history.

## v0.3.0 — Foundation

This first repository package contains:

- UI-based integration setup
- versioned trip data model
- atomic local JSON storage
- immutable raw GPS and odometer documents
- rebuildable route and statistics documents
- Douglas-Peucker route simplification
- basic WebSocket commands
- conservative legacy migration framework
- German and English translations
- tests and GitHub project templates

The interactive panel, map and Recorder import dialog follow after this foundation has been validated.

## Development installation

Copy `custom_components/trip_archive` to `/config/custom_components/trip_archive`, restart Home Assistant, then add **Trip Archive** under **Settings → Devices & services**.

Trip data is stored under `/config/trip_archive/` by default.

> Keep a Home Assistant backup while testing an early development version with irreplaceable data.

## License

MIT
