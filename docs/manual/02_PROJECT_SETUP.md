# 02 — Project Setup

## Standard Folder Structure
Use this structure for every project:

```
Project_Acronym_Year/
├── 00_ADMIN/
├── 01_RAWDATA/
│   ├── Field/
│   ├── Lab/
│   └── Geo/
├── 02_METADATA/
├── 03_CLEAN/
├── 04_ANALYSIS/
├── 05_RESULTS/
├── 06_PUBLICATION/
└── 07_ARCHIVE/
```

## Naming Conventions
Format: `Project_Acronym_Date_Version_Description`
- Date: `YYYY-MM-DD` (ISO-8601)
- Version: `v01`, `v02`, ... (semantic versions for code)
- Use lowercase, `_` or `-`; no spaces or special characters

## Onboarding Checklist (Project Start)
- [ ] Create project folder from template
- [ ] Assign Project Lead and Data Steward contact
- [ ] Initialize GitLab repository (enable LFS)
- [ ] Create `02_METADATA/README.md` and data dictionary stub
- [ ] Set up storage locations (NAS/Nextcloud paths)
- [ ] Register DMP in RDMO (if required by funder)
