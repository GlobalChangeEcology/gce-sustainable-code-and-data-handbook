# Data Organization Checklist

*Print and check off as you organize your project | Keep handy for daily reference*

## Project Setup ✅

### Folder Structure
- [ ] Created consistent folder hierarchy
- [ ] Used clear, descriptive folder names
- [ ] Separated raw data from processed data
- [ ] Created dedicated folders for scripts, results, and documentation
- [ ] Used standard naming conventions (no spaces, consistent case)

**Recommended structure:**
```
project_name/
├── data/
│   ├── raw/           # Original, untouched data
│   ├── processed/     # Cleaned, analysis-ready data
│   └── metadata/      # Data dictionaries, protocols
├── scripts/           # Analysis code
├── results/           # Outputs, figures, tables
├── docs/             # Documentation, protocols
└── README.md         # Project overview
```

### File Naming
- [ ] Used consistent naming convention across all files
- [ ] Included dates in ISO format (YYYY-MM-DD)
- [ ] Used version numbers for iterations (v01, v02)
- [ ] Avoided spaces and special characters
- [ ] Made names descriptive but not too long

**Good examples:**
- `2023-05-15_site_survey_data.csv`
- `temperature_analysis_v03.R`
- `species_counts_processed.csv`

**Bad examples:**
- `data.xlsx`
- `final version (1).csv`
- `Sarah's analysis - FINAL!!.R`

## Data Documentation ✅

### README File
- [ ] Created project README with overview
- [ ] Included project goals and objectives
- [ ] Listed all team members and roles
- [ ] Documented data collection methods
- [ ] Provided contact information
- [ ] Explained folder structure
- [ ] Listed software requirements
- [ ] Added last updated date

### Data Dictionary
- [ ] Created data dictionary for each dataset
- [ ] Defined all column names and meanings
- [ ] Specified units of measurement
- [ ] Documented coding schemes (e.g., 1=Yes, 0=No)
- [ ] Noted missing value codes (NA, -999, etc.)
- [ ] Included acceptable value ranges
- [ ] Added data collection dates and methods
- [ ] Listed data sources and citations

**Data dictionary template:**
| Column Name | Description | Units | Valid Values | Missing Code | Notes |
|-------------|-------------|-------|--------------|--------------|-------|
| site_id | Unique site identifier | - | SITE_001 to SITE_050 | - | Format: SITE_XXX |
| temperature | Air temperature | °C | -20 to 50 | NA | Measured at 2m height |

### Metadata Files
- [ ] Created metadata for each major dataset
- [ ] Documented collection protocols
- [ ] Recorded instrument calibration information
- [ ] Noted any changes in methods over time
- [ ] Included quality control procedures
- [ ] Listed known issues or limitations
- [ ] Added processing history

## Data Quality ✅

### Raw Data Protection
- [ ] Never modified original raw data files
- [ ] Stored raw data in read-only format when possible
- [ ] Created backup copies of raw data
- [ ] Documented any corrections in separate files
- [ ] Used version control for data processing scripts

### Data Validation
- [ ] Checked for missing values and handled appropriately
- [ ] Verified data types (dates, numbers, text)
- [ ] Identified and flagged outliers
- [ ] Checked for duplicated records
- [ ] Validated against expected ranges
- [ ] Cross-checked with field notes when available
- [ ] Documented all quality control steps

### Processing Documentation
- [ ] Created scripts for all data processing steps
- [ ] Used reproducible code (no manual Excel edits)
- [ ] Commented code thoroughly
- [ ] Saved intermediate processing steps
- [ ] Documented parameter choices and assumptions
- [ ] Created processing log/changelog

## File Management ✅

### Version Control
- [ ] Set up Git repository for project
- [ ] Added appropriate .gitignore file
- [ ] Used meaningful commit messages
- [ ] Created branches for experimental analyses
- [ ] Tagged important versions/milestones
- [ ] Pushed to remote repository (GitHub/GitLab)

### Backup Strategy
- [ ] Implemented 3-2-1 backup rule (3 copies, 2 different media, 1 offsite)
- [ ] Scheduled automatic backups
- [ ] Tested backup restoration process
- [ ] Documented backup procedures
- [ ] Assigned backup responsibilities to team members

### Access Control
- [ ] Set appropriate file permissions
- [ ] Documented who has access to what data
- [ ] Created shared access for team members
- [ ] Implemented security measures for sensitive data
- [ ] Regularly reviewed and updated access permissions

## Collaboration ✅

### Team Coordination
- [ ] Established file naming conventions for team
- [ ] Created shared workspace/repository
- [ ] Assigned clear roles and responsibilities
- [ ] Set up communication channels
- [ ] Scheduled regular check-ins
- [ ] Created onboarding process for new members

### Documentation Sharing
- [ ] Made documentation accessible to all team members
- [ ] Used common file formats (not proprietary)
- [ ] Created visual guides/diagrams when helpful
- [ ] Established update procedures for shared documents
- [ ] Archived old versions systematically

## Pre-Analysis Check ✅

### Data Readiness
- [ ] All data is in analysis-ready format
- [ ] Missing values are properly coded
- [ ] Variable types are correct
- [ ] Units are consistent across datasets
- [ ] Outliers have been reviewed and documented
- [ ] Quality flags are in place

### Analysis Preparation
- [ ] Analysis plan is documented
- [ ] Required software/packages are listed
- [ ] Computing environment is reproducible
- [ ] Sample size calculations are complete
- [ ] Statistical assumptions are documented

## Publication Preparation ✅

### Data Sharing Ready
- [ ] Removed or anonymized sensitive information
- [ ] Created public-ready dataset version
- [ ] Finalized data documentation
- [ ] Chose appropriate data repository
- [ ] Prepared data availability statement
- [ ] Assigned DOI to dataset if required

### Reproducibility Check
- [ ] All analysis code runs without errors
- [ ] Results can be reproduced from raw data
- [ ] All dependencies are documented
- [ ] Analysis environment is specified
- [ ] Computational methods are described

---

## Quick Quality Checks

**Daily:**
- [ ] Files saved in correct locations
- [ ] Progress documented in lab notebook
- [ ] Work backed up

**Weekly:**
- [ ] Data dictionary updated
- [ ] Version control commits made
- [ ] Team updated on progress

**Monthly:**
- [ ] Full backup tested
- [ ] Documentation reviewed and updated
- [ ] File organization assessed

**Before Publication:**
- [ ] Complete reproducibility test
- [ ] External review of documentation
- [ ] Data sharing compliance check

---

**Remember:** Good data organization saves time, prevents errors, and makes collaboration smoother. The time invested upfront pays dividends throughout the project lifecycle!

**Need help?** See the main handbook chapters on [Data Management](../02_data_management/01_introduction.md) and [Project Organization](../06_practical_tools/03_project_templates.md).

*Print this checklist and post it where you'll see it daily. Check off items as you complete them - you've got this!*