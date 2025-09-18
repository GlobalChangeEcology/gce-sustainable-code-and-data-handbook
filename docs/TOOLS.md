# Tools Overview

This page highlights the core tools and how we expect to use them in GCE projects. Keep choices pragmatic; prefer simple, well-supported tools.

## Source control & collaboration
- Git + GitHub: versioning, reviews, issues, releases. Use branches + PRs; protect `main`.
- Git LFS: for large binaries (add patterns in `.gitattributes`).
- Git Tutorial: Hands-on Slidev deck — see Tutorials → Git.

## Data management
- Frictionless: describe tabular datasets (Table Schema, Data Package); validate with `frictionless validate`.
- Pandera (Python) / pointblank (R): dataframe validation in pipelines.
- RDMO (optional): capture DMPs and project planning.

## Environments
- Python: Conda or Poetry; lock dependencies; pin major versions. Example: `environment.yml` or `pyproject.toml`.
- R: `renv::init()` and commit `renv.lock`.

## Reproducible workflows
- Snakemake: local/HPC-friendly, rule-based pipelines.
- Nextflow: scalable pipelines with containers and profiles.
- Containers: Docker/Podman for portability; bind data as volumes.

## Notebooks & docs
- Jupyter/Quarto: literate analysis. Export results to CSV/PNG for reuse.
- MkDocs Material: this site; use `docs/` for content and `mkdocs.yml` for nav.

## Publishing & archiving
- Datasets: Zenodo (general), PANGAEA (earth/environmental), GBIF (biodiversity).
- Software: GitHub Releases + `CITATION.cff`; archive on Zenodo for DOI.

---

See also: Decision Guide for tool selection and the Handbook chapters for detailed practices.
