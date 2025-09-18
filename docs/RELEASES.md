# Releases Checklist

Follow this checklist when publishing a new version of the handbook or examples.

## Before releasing
- Update content and navigation
- Validate the site locally: `mkdocs build` (fix warnings due to `--strict`)
- Update `CITATION.cff` (version, date)
- Update `CHANGELOG.md` (if present)

## Tag and release
- Create a Git tag using semantic versioning (e.g., `v1.0.0`)
- GitHub → Releases → "Draft a new release"
  - Tag: `vX.Y.Z`
  - Title: concise summary
  - Notes: highlight changes and contributors
- Publish the release

## Archive and DOI (Zenodo)
- Ensure the repo is connected in Zenodo settings
- Publishing the GitHub Release will archive and mint/update the DOI
- Add/update the DOI badge in README and site homepage

## After releasing
- Verify the Pages site contains the new content
- Announce internally and update any external links
- Create issues for follow-ups and improvements
