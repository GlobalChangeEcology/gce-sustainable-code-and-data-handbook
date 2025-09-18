# 06 — Data Quality

## Quality Objectives
- Accuracy, completeness, consistency, timeliness, and traceability.

## Validation & Checks
- Define a schema (types, ranges, allowed values) per dataset.
- Automate checks using Frictionless (Table Schema) or pandera (Python) / pointblank (R).
- Add unit tests for critical transformations.

## QA Process
- Ingestion QA: verify file integrity, row/column counts, missing values.
- Cleaning QA: before/after summaries, outlier review, sampling spot checks.
- Peer review QA via MR; track issues and resolutions.

## Audit Trail
- Log changes in README/CHANGELOG with dates and authors.
- Keep scripts in version control; avoid manual spreadsheet edits.

## Acceptance Criteria
- Dataset must pass automated schema checks.
- README + data dictionary complete; license and citation provided.
- Sensitive data reviewed against policy before publication.
