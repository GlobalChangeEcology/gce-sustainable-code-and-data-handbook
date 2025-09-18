# Basics — Reproducibility 101

Practical essentials to make your research sustainable and reproducible.

## Environments
- Choose a manager (Conda, Poetry, renv) and commit lockfiles
- Document how to create/activate the environment in README
- For workflows, use per-rule envs (Snakemake) or profiles (Nextflow)

## Metadata
- Always include a dataset `README.md` and `data_dictionary.csv`
- Use a schema (Frictionless) to validate shape and types
- Keep provenance: who/when/how; link to scripts and pipelines

## Licensing
- Data: CC BY 4.0 by default; Software: MIT by default
- Dual-license repos when both code and templates/docs exist
- Add `CITATION.cff` and link to Zenodo for DOI on releases

## Minimal checklist
- [ ] Environment file committed (`environment.yml`, `renv.lock`, or `poetry.lock`)
- [ ] Dataset docs present (`README.md`, `data_dictionary.csv`) and up-to-date
- [ ] License files present (MIT, CC BY), copyright accurate
- [ ] CITATION.cff present; Zenodo linked for DOI on release
- [ ] Automated build/tests/docs run in CI

See also:
- Basics: [FAIR in Practice](FAIR.md)
- Handbook: Metadata & Documentation, Data Quality, Publishing & Reuse
- Tutorials: Conda, Snakemake, GitHub Actions
