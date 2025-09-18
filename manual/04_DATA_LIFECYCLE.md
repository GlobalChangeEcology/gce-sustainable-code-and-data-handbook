# 04 — Data Lifecycle

This section defines required practices across the data lifecycle.

## 1) Plan
- Define objectives, data types, sensitivity, and responsibilities.
- Register or update a DMP (e.g., in RDMO) if required.
- Decide storage locations and access groups.

## 2) Collect / Ingest
- Store new raw data in `01_RAWDATA/` (immutable).
- Capture acquisition context in `02_METADATA/README.md` (who/what/when/where/how).
- Use consistent file naming and timestamps (UTC for instruments).

## 3) Organize
- Maintain the standard folder structure; do not mix raw and derived data.
- Add or update `data_dictionary.csv` for new tabular datasets.
- Log external data sources with citation and license.

## 4) Clean / Transform
- Work on copies in `03_CLEAN/` only; never edit `01_RAWDATA/`.
- Use scripted transformations (R/Python); save scripts in `04_ANALYSIS/`.
- Record provenance in `README.md` (inputs → steps → outputs).

## 5) Analyze
- Keep analysis code under Git with branches and MRs.
- Capture environments (Conda/renv) or container recipes.
- Prefer pipeline tools (Snakemake/Nextflow) for reproducibility.

## 6) Review
- Peer review analysis and data changes using Merge Requests.
- Run automated checks (schema validation, tests, linting) in CI.

## 7) Publish
- Prepare a release package: cleaned data, README, dictionary, code snapshot, environment.
- Choose repository (Zenodo/PANGAEA/GBIF/Dryad) and license.
- Obtain DOI and draft citation text.

## 8) Archive & Preserve
- Copy finalized data + README to `07_ARCHIVE/`.
- Ensure long-term storage on university-managed infrastructure.
- Document retention periods; verify restore via periodic test restores.
