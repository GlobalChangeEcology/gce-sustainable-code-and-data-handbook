# 08 — Tools & Platforms

## Storage & Backup
- Primary storage: University NAS/HPC; automatic backups managed by IT.
- Collaboration: Nextcloud for files that require sharing/sync.
- Do not store research data on personal devices.

## Computing & Analysis
- Python (Conda/Poetry), R (renv), Jupyter/Quarto for notebooks/reports.
- Workflow management: Snakemake or Nextflow for pipelines.
- Geospatial: GDAL, QGIS; remote sensing libraries (rasterio, xarray).

## Validation & Metadata
- Frictionless Data (frictionless-py) for schema & data package.
- Pandera (Python) / pointblank (R) for data validation.
- Metadata: Markdown READMEs, Dublin Core elements, CITATION.cff.

## Version Control & CI/CD
- GitLab with protected branches and MR reviews.
- Enable Git LFS; add CI pipelines for tests and checks.

## Publishing
- Zenodo integration for DOIs; domain repositories (PANGAEA, GBIF, Dryad).
