# 05 — File & Version Control

## Git/GitLab Workflow (Code & Text)
- Default branches: `main` (protected), `develop` (optional), feature branches.
- Use Merge Requests with mandatory review before merging to `main`.
- Tag releases: `vMAJOR.MINOR.PATCH` with changelog.
- Use Git LFS for large binaries (e.g., `.tif`, `.nc`, `.h5`, `.zip`).

## Data Versioning Conventions
- Raw data are immutable; corrections documented as new files with versioned names.
- Cleaned datasets include a version in the filename and README (e.g., `v01`).
- Maintain a CHANGELOG in `02_METADATA/` for major dataset updates.

## Reproducible Environments
- Python: Conda/Poetry with `environment.yml` or `pyproject.toml`.
- R: `renv.lock` committed; optionally rocker/Apptainer images.
- Pin versions in environment files; document OS/CPU/GPU constraints.

## Releases and DOIs
- Create a GitLab Release for major milestones.
- Connect GitLab to Zenodo for automatic DOI minting on release (optional).
- Include `CITATION.cff` and a release checklist in the repository.
