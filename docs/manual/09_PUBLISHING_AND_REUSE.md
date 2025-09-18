# 09 — Publishing & Reuse

## Repository Selection
- General-purpose: Zenodo (code+data, DOI).
- Environmental/Earth: PANGAEA.
- Biodiversity/occurrence: GBIF (via IPT/publisher).
- Life sciences: Dryad.

## Licensing
- Default: CC-BY 4.0 for data unless restricted; MIT/BSD for code.
- Respect third-party licenses; document any limitations.

## Submission Package
- Cleaned data with versioned filenames.
- `README.md` and `data_dictionary.csv`.
- Code snapshot and environment files (or container recipe).
- Citation text and contributors.

## DOI & Citation
- Mint DOI on release; include in publications.
- Example citation format:
  "Author(s) (Year). Title. Repository. DOI"

## Embargo & Access
- Use embargo periods when needed; state release date.
- For sensitive data, publish metadata with controlled access to data.

## Minting a DOI with Zenodo (GitHub integration)

1) Prepare your repo
- Ensure a clear license (`LICENSE.md`) and a `CITATION.cff` with authors, title, and preferred citation.
- Tag README sections for "How to cite" and link the DOI badge once minted.

2) Link GitHub → Zenodo
- Go to https://zenodo.org/account/settings/github/ and enable the repository.
- Choose "Create a new record on release" so each GitHub Release archives a snapshot and gets a DOI.

3) Create a GitHub Release
- From GitHub → Releases → "Draft a new release".
- Use semantic versioning (e.g., v1.0.0) and describe what changed.
- Publish the release; Zenodo will capture it and assign a version DOI and a concept DOI.

4) Update badges
- Add the DOI badge Zenodo provides to your README and site homepage.
- Keep `CITATION.cff` in sync with new versions (authors, title, version).

### What to publish where
- Datasets (tabular): Zenodo (general), PANGAEA (earth/env), GBIF (biodiversity occurrences), institutional or national repositories as required.
- Software: GitHub Releases + Zenodo DOI; publish to PyPI/Conda/R-universe if distributing packages.
- Notebooks and docs: include as artifacts in the release; link to a persistent archive.

### `CITATION.cff` essentials
- Minimum fields: `cff-version`, `message`, `title`, `authors`, `date-released`, `version`. Optional: `doi`, `identifiers`, `repository-code`.
- Validate with https://citation-file-format.github.io/

### License and metadata
- Use SPDX identifiers (e.g., MIT, Apache-2.0, CC-BY-4.0) and include license files.
- Provide machine-readable metadata where possible (Frictionless `datapackage.json`, `table_schema.json`).
