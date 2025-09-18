---
title: Deposit & Validation Recipes
---

# Deposit & Validation Recipes

## Zenodo (via GitHub Releases)

- Enable in repository: Settings → GitHub Pages and Releases are already set; link Zenodo to the GitHub repo at https://zenodo.org/account/settings/github/ and flip the toggle.
- Create a GitHub Release; Zenodo will mint a DOI automatically for the release and a concept DOI for the project.
- Provide CITATION.cff, LICENSE, and an exportable README with how to use the artifact.

```yaml
# .github/workflows/release.yml (snippet)
on:
  push:
    tags:
      - 'v*.*.*'
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build artifact
        run: |
          tar -czf artifact.tgz docs site || true
      - uses: softprops/action-gh-release@v2
        with:
          files: artifact.tgz
```

## Dataverse (API upload)

```bash
DV_BASE=https://demo.dataverse.org
API_TOKEN=<your_token>
DATASET_PID="doi:10.5072/FK2/XXXXXX"
FILE=results.zip

curl -H "X-Dataverse-key: $API_TOKEN" \
  -F "file=@$FILE" \
  "$DV_BASE/api/datasets/:persistentId/add?persistentId=$DATASET_PID"
```

Tips: include README, data dictionary, codebook; set file tags (Tabular, Documentation); attach provenance as JSON or text.

## Validators in CI

```yaml
# .github/workflows/validate.yml
name: Validate data and metadata
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install validators
        run: |
          pip install frictionless pandera
          # optional: bids-validator via node or container
      - name: Validate tabular schemas (Frictionless)
        run: |
          frictionless validate docs/examples/minimal-project/data/datapackage.json
      - name: Run pandera tests
        run: |
          python docs/examples/minimal-project/scripts/validate_pandera.py
```

### BIDS Validator (container)

```yaml
  bids:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate BIDS dataset
        run: |
          docker run --rm -v "$PWD:/data:ro" bids/validator /data/path/to/bids
```

### Darwin Core checks (GBIF IPT)

- Use IPT’s preview/data quality; locally, verify headers match DwC terms and run CSV schema checks with Frictionless.

```bash
frictionless describe occurrence.csv > schema.json
frictionless validate occurrence.csv --schema schema.json
```

Cross‑links: Guided Project Phases 9–10; Data Versioning; Ethics & Consent.
