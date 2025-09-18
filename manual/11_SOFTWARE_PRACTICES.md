# 11 — Software Practices (Sustainable Code)

Practical guidance for writing maintainable, reviewable, and reusable research code.

## Core Practices
- Version control: Git with feature branches, small PRs, and reviews.
- Documentation: README, inline docstrings, minimal examples.
- Testing: Unit tests for critical functions; smoke tests for pipelines.
- Environments: Pin dependencies (Conda/Poetry/renv); use lock files.
- Automation: Makefiles or task runners; CI for tests and linting.
- Packaging: Structure code as packages/modules; semantic versioning.

## Language-specific Tips
- Python: `pyproject.toml`, `ruff`/`black` lint/format, `pytest`, `tox` (optional).
- R: `renv`, `testthat`, `lintr`, `targets` for pipelines.

## Reproducible Workflows
- Use Snakemake/Nextflow or R `targets` to codify steps and dependencies.
- Save intermediate artifacts deterministically; avoid manual steps.
- Capture parameters/config in YAML/TOML files.

## Collaboration
- Code reviews: focus on clarity, correctness, and performance where relevant.
- Issues and milestones: track tasks and releases.
- Contribution guidelines: define style, tests, and DCO/CLA if needed.

## Sustainability & Archival
- Release code with a tag and `CITATION.cff`; archive on Zenodo for DOI.
- Include a minimal dataset or synthetic data for examples/tests.
- Add maintenance status in README and an OWNER file.

## Checklist
See `manual/templates/software_practices_checklist.md`.
