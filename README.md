# Trip Archive

![Beta](https://img.shields.io/badge/status-beta-orange)
![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2025.6%2B-41BDF5)
![License](https://img.shields.io/badge/license-MIT-green)

Archive completed journeys from **Home Assistant Recorder** and explore them later using an interactive map, travel statistics and permanently stored trip data.

> ⚠️ **Beta Software**
>
> Trip Archive is currently in **Beta (v0.3.0-beta.1)**.
> The complete Recorder-to-Archive workflow is implemented and stable, but the project is still evolving before its first stable release.

---

# Dashboard

> *(Screenshot will appear here after uploading `docs/images/dashboard.png`.)*

![Trip Archive Dashboard](docs/images/dashboard.png)

Trip Archive permanently preserves completed journeys outside the Recorder database and provides an interactive map together with detailed travel statistics.

---

# Why Trip Archive?

Home Assistant Recorder is designed for short-term history. Depending on your Recorder settings, older location history is automatically removed over time.

Trip Archive solves this by creating permanent trip archives directly from Recorder data.

Unlike GPX import tools, Trip Archive does **not** rely on exported files or external services.

Recorder is the **only source of trip data**.

The archived raw GPS data always remains unchanged.

Display routes, statistics and map visualizations are derived from this immutable data and can be recreated at any time.

---

# Features

## Archive

- Archive completed trips directly from Home Assistant Recorder
- Preserve immutable original GPS data
- Optional odometer support
- Permanent local trip storage

## Explore

- Interactive map view
- Travel statistics
- Simplified display routes
- Segment visualization
- Trip overview sidebar
- Responsive desktop and mobile layout

## Reliability

- Fully local operation
- No cloud services
- No external accounts
- No GPX imports
- No Garmin imports
- No OwnTracks imports
- Reproducible statistics
- Immutable archived data

---

# Installation

## Manual Installation

1. Download the latest release from the GitHub Releases page.
2. Copy the **trip_archive** integration into:

```text
/config/custom_components/
```

3. Restart Home Assistant.
4. Open:

```text
Settings → Devices & Services
```

5. Click **Add Integration**.
6. Search for **Trip Archive**.

> **HACS support is planned for a future release.**

---

# Requirements

Trip Archive requires:

- Home Assistant
- Home Assistant Recorder
- Recorded location history
- At least one tracked location entity

Trips can only be archived after they have been recorded by Home Assistant Recorder.

---

# Architecture

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

Recorder is the **only** source of trip data.

Archived raw data never changes.

Everything displayed inside the dashboard is generated from this immutable archive.

This guarantees reproducible statistics and routes.

---

# Local Storage

Archived trips are stored locally inside Home Assistant.

```text
/config/trip_archive/trips/
```

Each trip is independent and can safely be deleted without affecting Recorder.

---

# Reference Validation

Trip Archive has been validated using a real-world reference journey.

## Scotland 2026

| Item | Value |
|------|------:|
| Distance | **4,455 km** |
| Original GPS points | **21,984** |
| Display points | **1,869** |
| Segments | **1** |
| Start odometer | **22,334 km** |
| End odometer | **26,789 km** |

This journey is used during development to verify statistics, route generation and data integrity.

---

# Documentation

- CHANGELOG
- ROADMAP
- CONTRIBUTING
- RELEASE_CHECKLIST

---

# Roadmap

Planned improvements include:

- HACS support
- Additional statistics
- Performance improvements
- Additional language translations

---

# Contributing

Bug reports, feature requests and pull requests are always welcome.

Please open a GitHub Issue if you discover a bug or have an idea for improvement.

---

# License

MIT License

---

Made with ❤️ for the Home Assistant community.
