# GCE Sustainable Code & Data Handbook

Guidance, templates, and checklists for building durable, maintainable code and managing FAIR, reusable data at the Chair of Global Change Ecology (University of Würzburg). Focus areas: code quality, environments, reproducible workflows, dataset documentation, publishing, and sustainability.

- Live manual: see the `manual/` folder
- Templates: see `manual/templates/`
- Department rollout: see `IMPLEMENTATION_GUIDE.md`

## Why this exists
- Make code and data easier to maintain, review, and reuse
- Align with FAIR and DFG good scientific practice
- Reduce risk and increase reproducibility across projects

## What’s inside
- Policy & Principles, Project Setup, Metadata & Documentation
- Data Lifecycle, File & Version Control, Data Quality
- Sensitive Data, Tools & Platforms, Publishing & Reuse
- Software Engineering Practices and Checklists
- Implementation Guide for department-wide adoption

## Folder structure
```
manual/
  01_POLICY_AND_PRINCIPLES.md
  02_PROJECT_SETUP.md
  03_METADATA_AND_DOCUMENTATION.md
  04_DATA_LIFECYCLE.md
  05_FILE_AND_VERSION_CONTROL.md
  06_DATA_QUALITY.md
  07_SENSITIVE_DATA.md
  08_TOOLS_AND_PLATFORMS.md
  09_PUBLISHING_AND_REUSE.md
  10_CHECKLISTS_AND_TEMPLATES.md
  templates/
    README_dataset.md
    PROJECT_README.md
    data_dictionary.csv
    DMP_outline.md
    checklist_project_start.md
    checklist_ongoing.md
    checklist_closure.md
    qa_checklist.md
    CITATION.cff
    Snakefile
    environment.yml
IMPLEMENTATION_GUIDE.md
```

## How to use
- Start new projects with the standard structure (see 02 Project Setup)
- Create a dataset README and data dictionary for each dataset
- Keep raw data immutable; script all transformations
- Use Git/GitLab, enable LFS for large files, and review via MRs
- Publish cleaned data and code with a DOI at project milestones

## Contributing
Contributions are welcome via Pull Requests. Please read `CONTRIBUTING.md` and follow the Code of Conduct.

## License
- Documentation and templates: CC BY 4.0
- Code samples and pipeline skeletons: MIT
See `LICENSE.md` for details.

## Acknowledgements
Developed by the Chair of Global Change Ecology, University of Würzburg.
