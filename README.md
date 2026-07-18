# Trip Archive

[![Latest release](https://img.shields.io/github/v/release/Tritschi/trip-archive?include_prereleases&label=release)](https://github.com/Tritschi/trip-archive/releases)
![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2025.6%2B-41BDF5)
![License](https://img.shields.io/badge/license-MIT-green)

Archive completed journeys from **Home Assistant Recorder** and explore them later using interactive maps, travel statistics and permanently stored trip data.

> ⚠️ **Beta Software**
>
> Trip Archive is currently in **beta**. The release badge above always points to the latest published version.
> The complete Recorder-to-Archive workflow is implemented and stable, but the project will continue to evolve before the first stable release.

---

## Dashboard

![Trip Archive Dashboard](docs/images/dashboard.png)

Trip Archive permanently preserves completed journeys outside the Recorder database and provides an interactive map together with detailed travel statistics.

---

## Why Trip Archive?

Home Assistant Recorder is designed for short-term history. Depending on your Recorder settings, older location history is automatically removed over time.

Trip Archive solves this by creating permanent trip archives directly from Recorder data.

Unlike GPX import tools, Trip Archive does **not** rely on exported files or external services.

**Recorder is the only source of trip data.**

The original archived GPS data always remains unchanged.

Display routes, statistics and map visualizations are derived from this immutable data and can always be recreated.

---

## Features

### Archive

- Archive completed trips directly from Home Assistant Recorder
- Preserve immutable original GPS data
- Optional odometer support
- Permanent local trip storage

### Explore

- Interactive map view
- Travel statistics
- Simplified display routes for fast rendering
- Segment visualization
- Trip overview sidebar
- Responsive desktop and mobile layout

### Reliability

- Fully local operation
- No cloud services
- No external accounts
- No GPX imports
- No Garmin imports
- No OwnTracks imports
- Immutable archived data
- Reproducible statistics and display routes

---

## Installation

### Manual Installation

1. Download the latest release from the GitHub Releases page.
2. Copy the **trip_archive** folder into:

```text
/config/custom_components/
```

3. Restart Home Assistant.
4. Open **Settings → Devices & Services**.
5. Click **Add Integration**.
6. Search for **Trip Archive**.

> **HACS support is planned for a future release.**

---

## Requirements

Trip Archive requires:

- Home Assistant
- Home Assistant Recorder
- Recorded location history
- At least one tracked location entity

Trips can only be archived after they have been recorded by Home Assistant Recorder.

---

## Architecture

```text
Home Assistant Recorder
           │
           ▼
      Trip Archive
           │
           ├── Immutable archived GPS data
           ├── Display route generation
           ├── Travel statistics
           └── Interactive map
```

Trip Archive intentionally follows a simple design philosophy.

Recorder is the **only** source of trip data.

Archived raw data never changes.

Everything displayed in the dashboard—including statistics, display routes and map visualization—is generated from this immutable archive.

This guarantees reproducible results at any time.

---

## Local Storage

Archived trips are stored locally inside Home Assistant:

```text
/config/trip_archive/trips/
```

Each trip is stored independently and can be viewed or deleted without affecting Home Assistant Recorder.

---

## Reference Validation

Trip Archive has been validated using a real-world reference journey.

### Scotland 2026

| Item | Value |
|------|------:|
| Total distance | **4,455 km** |
| Original GPS points | **21,984** |
| Display points | **1,869** |
| Segments | **1** |
| Start odometer | **22,334 km** |
| End odometer | **26,789 km** |

This reference trip is used during development to verify route generation, statistics and data integrity.

---

## Documentation

Additional project documentation is available in this repository:

- [CHANGELOG](CHANGELOG.md)
- [ROADMAP](ROADMAP.md)
- [CONTRIBUTING](CONTRIBUTING.md)
- [RELEASE CHECKLIST](RELEASE_CHECKLIST.md)

Documentation will continue to grow throughout the beta phase.

---

## Roadmap

Planned improvements include:

- HACS support
- Additional statistics
- Performance improvements
- Additional language translations

Future priorities may evolve based on community feedback.

---

## Contributing

Bug reports, feature requests and pull requests are always welcome.

If you discover a bug or have an idea for improvement, please open a GitHub Issue.

---

## License

This project is licensed under the **MIT License**.

---

Made with ❤️ for the Home Assistant community.
