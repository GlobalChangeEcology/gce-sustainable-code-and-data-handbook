# Implementation Guide — Data Management at GCE

This guide explains how to adopt the manual across the department.

## Objectives
- Ensure consistent, high-quality data management aligned with FAIR and DFG.
- Reduce risk of data loss and improve reproducibility and reuse.

## Roles & Responsibilities
- Project Lead: accountable for compliance and resources.
- Data Steward: owner of policy, training, reviews, and support.
- IT/Infrastructure: storage, backup, and access management.
- All Staff: follow standards, complete checklists, and maintain metadata.

## Rollout Phases
1) Preparation (Weeks 1–2)
- Approve policy (01) and baseline requirements.
- Create GitLab group templates and Nextcloud/NAS group folders.
- Publish manual and templates to department space.

2) Pilot (Weeks 3–8)
- Select 2–3 active projects; migrate to standard structure.
- Run checklists and capture feedback.
- Set up CI checks (schema validation) on one project.

3) Department-wide Launch (Month 3)
- Require standard structure for all new projects.
- Training: 60-min intro + 90-min hands-on (folder structure, README, dictionary, Git basics).
- Office hours weekly for support.

4) Consolidation (Months 4–6)
- Migrate legacy projects opportunistically (when active).
- Track metrics and address gaps; refine templates.

## Minimal Technical Setup
- Storage: NAS/HPC with nightly backups; Nextcloud for sharing.
- Version Control: GitLab with protected `main`, LFS enabled, group-level templates.
- Validation: frictionless/pandera checks optional in CI.
- Publishing: Zenodo or domain repository; DOI on releases.

## Checkpoints & Metrics
- % projects with `README.md` + `data_dictionary.csv`.
- % releases with DOIs and complete submission package.
- Backup verification success rate (monthly).
- Training completion for new members.

## Governance & Change Control
- Manual lives in version control; updates via Merge Requests.
- Review cadence: every 6 months; emergency updates as needed.
- Data Steward publishes a changelog and announces updates.

## Quick Start for New Projects
1. Create folder using standard structure.
2. Fill `PROJECT_README.md` and dataset `README.md` + `data_dictionary.csv`.
3. Initialize Git repo; enable LFS; push to GitLab.
4. Capture environment (Conda/renv) and add pipeline (optional).
5. At milestones, create a release and archive in `07_ARCHIVE/`.

## Tooling Options (Choose-Your-Own-Stack)
- Python + Conda + Snakemake + frictionless + pandera
- R + renv + targets/drake + pointblank
- Mixed: Notebooks (Jupyter/Quarto), QGIS, GDAL for geospatial

## Support
- Contact: Data Steward (email here)
- Training calendar and office hours: link here
- FAQs: add/link as the program matures
