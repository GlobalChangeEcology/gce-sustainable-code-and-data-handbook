# Example — Minimal Project

This small example shows the folder layout and a tiny workflow.

## Structure
```
Project_Acronym_Year/
├── 01_RAWDATA/
├── 02_METADATA/
├── 03_CLEAN/
├── 04_ANALYSIS/
├── 05_RESULTS/
└── 06_PUBLICATION/
```

## Steps
1. Place a small CSV in `01_RAWDATA/`.
2. Create a cleaned version in `03_CLEAN/` (fix headers, types, etc.).
3. Run a simple summary script (Python or R) from the quick starts.
4. Save results to `05_RESULTS/`.

## Learn
- How to separate raw and clean data
- Where to put scripts and results
- How to document with README and a data dictionary

# Minimal Example Dataset

This example demonstrates a tiny, well-documented dataset with a corresponding data dictionary and simple summary scripts.

## Dataset
- Path: `docs/examples/minimal-project/data/example.csv`
- Description: four rows with `id` and `value`.

## Documentation files
- `README.md` (this file): describes purpose, structure, and provenance
- `data_dictionary.csv`: column-level metadata (name, type, description, allowed)

## Provenance
- Created for demonstration purposes on 2025-09-18
- Owner: GCE Handbook Team
- License: CC BY 4.0

## How to use
- Python: run `python summarize.py` (requires `pandas`)
- R: run `Rscript summarize.R` (requires `readr`, `dplyr`)

## Columns
- `id` (integer): row identifier
- `value` (float): numeric value to summarize
