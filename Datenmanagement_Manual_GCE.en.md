# 📘 Data Management Manual  
### Chair of Global Change Ecology – University of Würzburg  

> For the full, living manual and templates, see `manual/`.  
> For rollout details, see `IMPLEMENTATION_GUIDE.md`.

---

## 1. Why Data Management?

Good data management is the foundation of successful research.  
It ensures that:
- Data are findable and understandable.  
- Results remain reproducible.  
- Knowledge is not lost when people leave the chair.  
- Funding requirements (DFG, EU, BMBF) are met.  

👉 Guiding principles: **FAIR** = Findable, Accessible, Interoperable, Reusable  

---

## 2. Roles and Responsibilities

- **Project Lead**  
  Responsible for data quality and documentation.  

- **Data Steward (chair, e.g., data manager)**  
  Coordinates data management, provides support, enforces standards.  

- **All Staff Members**  
  Store their data according to this manual and maintain metadata.  

---

## 3. Standard Project Folder Structure

Each project receives a main folder following the pattern:  
`ProjectName_Acronym_Year`

```
Project_Acronym_Year/
│
├── 00_ADMIN/             # Contracts, permits, project description
├── 01_RAWDATA/           # Raw data (unchanged!)
│   ├── Field/
│   ├── Lab/
│   └── Geo/
├── 02_METADATA/          # README, documentation, methods
├── 03_CLEAN/             # Cleaned / standardized data
├── 04_ANALYSIS/          # Scripts, workflows, models
├── 05_RESULTS/           # Tables, figures, statistics
├── 06_PUBLICATION/       # Papers, posters, presentations
└── 07_ARCHIVE/           # Final archive for repositories
```

👉 Advantage: All projects have the same structure → less searching.  

---

## 4. File Naming Conventions

Rule:  
`Project_Acronym_Date_Version_Description`

**Examples:**  
- `GCE_FieldData_2023-05-12_v01.csv`  
- `GCE_LabNutrients_2023_v02.xlsx`  
- `GCE_RemoteSensing_Landsat8_DE_2019_v01.tif`  

👉 No special characters, no spaces. Use lowercase, `_` or `-` only.  

---

## 5. Documentation (Metadata)

Each dataset requires a **README.md** in the same folder.  

### Template for README.md
```markdown
# Project Title / Dataset Name

**Created by:** Name, Email  
**Date:** DD.MM.YYYY  
**Version:** v01  

## Description
Brief description of what the data contain.

## Methodology
How were the data collected (field, lab, satellite, model)?  
Which devices/software?

## Data Structure
- Column 1: Variable X (unit, description)  
- Column 2: Variable Y (unit, description)  

## Quality Assurance
How were data checked, validated, cleaned?

## License / Rights
e.g., CC-BY 4.0, internal use, etc.

## Contact
Who is responsible for inquiries?
```

---

## 6. Tools & Workflows

- **Code versioning:** Git / GitLab (use central repositories).  
- **File management:** University servers or Nextcloud → no private laptops.  
- **Large data volumes:** Central NAS or HPC storage.  
- **Documentation:** Markdown/plain text → more durable than Word files.  

---

## 7. Backup & Archiving

- **During the project:** Automatic backup (university server/cloud).  
- **After project completion:** Data + metadata → `07_ARCHIVE`.  
- **Publish long-term in repositories:**  
  - [PANGAEA](https://www.pangaea.de) – Environmental & Earth system data  
  - [Zenodo](https://zenodo.org) – general, DOI, also for code  
  - [Dryad](https://datadryad.org) – life sciences  
  - [GBIF](https://www.gbif.org) – biodiversity data  

---

## 8. Project Checklist

✅ **Project start**  
- Create project folder using the standard structure.  
- Appoint a person responsible for data management.  

✅ **During the work**  
- Never overwrite raw data.  
- Edit only copies in `03_CLEAN`.  
- Store every file with a descriptive name.  
- Keep the metadata README up to date.  

✅ **Project completion**  
- Move finalized data + README to `07_ARCHIVE`.  
- Upload data to a repository and obtain a DOI.  
- Cite the DOI in publications.  

---

## 9. Quick Wins – implement now

1. Start new projects with the **standard folder structure**.  
2. **README.md** mandatory for all datasets.  
3. Use consistent file names following the convention.  

This immediately creates more transparency—even when starting small.  

---

✍️ **Contact person at the chair:**  
Data Steward (e.g., [Your Name])  
Email: [your email address]
