# Release checklist

Use this checklist before uploading a new version through the GitHub web interface.

## Version consistency

Confirm that the same release number appears in all relevant places:

- `custom_components/trip_archive/manifest.json`
- `README.md`
- newest section of `CHANGELOG.md`
- release-note file
- install ZIP filename
- repository ZIP filename
- GitHub tag and release title

## Repository content

- README describes the version being uploaded
- Changelog contains the new release at the top
- Roadmap reflects the current development phase
- No `__pycache__`, `.pytest_cache`, temporary files or local test output
- No archived personal trip data
- Integration is located below `custom_components/trip_archive/`

## Install package

- ZIP contains one `trip_archive` folder
- `manifest.json` contains the current version
- frontend JavaScript contains the intended final UI
- existing `/config/trip_archive/` data is not part of the package

## GitHub web upload

1. Upload the extracted repository files and commit them.
2. Open the repository homepage and verify the rendered README.
3. Only after that, create the GitHub release and tag.
4. Attach the install ZIP.
5. Mark beta versions as pre-release.
6. Download the published ZIP once and test the real installation path.
