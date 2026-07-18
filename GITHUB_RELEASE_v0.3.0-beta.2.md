# Trip Archive v0.3.0-beta.2

This quality release aligns the GitHub repository with the complete Home Assistant integration and establishes a consistent release foundation.

## Highlights

- Complete integration source is now included in the repository
- `manifest.json` is the single maintained source of the integration version
- Dashboard and Python runtime read the version dynamically
- README is version-independent
- Repository and installation package contain the same integration code
- Generated Python bytecode is excluded

## Installation

Copy the `trip_archive` folder from the installation archive to `/config/custom_components/`, then restart Home Assistant.

This is a beta release. Back up your Home Assistant configuration before testing.
