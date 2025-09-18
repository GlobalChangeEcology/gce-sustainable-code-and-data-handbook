# Quick Start — R

## 1) Environment
Install packages and initialize renv:
```r
install.packages(c("renv","readr","dplyr","pointblank"))
renv::init()
```

## 2) Data dictionary
Create `data_dictionary.csv`:
```
name,type,unit,description,allowed_values,missing_values
id,integer,,Unique identifier,,
value,number,unitless,Example measurement,,
```

## 3) Validate data (optional)
```r
# validate.R
library(pointblank)

agent <- create_agent(readr::read_csv("03_CLEAN/example.csv")) %>%
  col_is_integer("id") %>%
  col_exists("value")

invisible(interrogate(agent))
```

## 4) Reproducible script
```r
# summarize.R
library(readr); library(dplyr)
read_csv("03_CLEAN/example.csv") %>%
  summarize(mean_value = mean(value, na.rm = TRUE), n = n()) %>%
  readr::write_csv("05_RESULTS/summary.csv")
```

## 5) Run
```bash
Rscript validate.R
Rscript summarize.R
```

## 6) Next
- Snapshot environment: `renv::snapshot()`
- Commit and push
- Consider `targets` for pipelines as projects grow
