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

## Practical validation examples

### Python: pandera schema
```python
import pandas as pd
import pandera as pa
from pandera import Column, DataFrameSchema, Check

schema = DataFrameSchema({
    "id": Column(int, Check.ge(1)),
    "value": Column(float, [Check.ge(0), Check.le(10)])
})

df = pd.read_csv("docs/examples/minimal-project/data/example.csv")
schema.validate(df)  # raises if invalid
```

### R: pointblank agent
```r
library(readr)
library(pointblank)

df <- readr::read_csv("docs/examples/minimal-project/data/example.csv", show_col_types = FALSE)
agent <- create_agent(read_fn = ~ df) |>
  col_is_integer(vars(id)) |>
  col_vals_between(vars(value), left = 0, right = 10)

agent |> interrogate()
```
