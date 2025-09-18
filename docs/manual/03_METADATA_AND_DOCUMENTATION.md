# 03 — Metadata & Documentation

## Dataset README
Each dataset directory must contain a `README.md` covering:
- Title, description, authors, contact
- Date, version, license
- Methods and instruments/software
- Data structure (variables, units, descriptions)
- QA/validation steps
- Provenance and limitations

See template in `manual/templates/README_dataset.md`.

## Data Dictionary (Codebook)
- Provide a machine- and human-readable schema of variables.
- Prefer CSV/TSV with columns: `name`, `type`, `unit`, `description`, `allowed_values`, `missing_values`.
- Link the dictionary in the dataset `README.md`.

## Project-level Documentation
- `02_METADATA/PROJECT_README.md`: scope, team, dependencies, milestones
- `CITATION.cff`: how to cite the project
- `LICENSE`: default CC-BY 4.0 for data unless restricted

## Metadata Standards
- General: Dublin Core elements for citation-level metadata
- Tabular data: Frictionless Data (Table Schema / Data Package)
- Biodiversity: Darwin Core (DwC)
- Geospatial: ISO 19115/19139; include CRS, bounding box, and resolution
