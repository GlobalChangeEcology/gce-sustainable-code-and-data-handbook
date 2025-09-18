---
title: Findability & Discovery (Beginner)
---

# Findability & Discovery (Beginner)

Goal: make your dataset and code easy to find and cite without knowing any web standards.

1) Choose the right repository first
- Discipline repository beats generalist: biosciences → ENA/GEO/PRIDE/GBIF; geospatial → PANGAEA/Community catalogs; otherwise Zenodo/Dataverse.
- Check their required fields and validators — pass them before publishing.

2) Provide a great landing page
- Clear title, 2–3 sentence abstract, keywords, authors (ORCID), funding, related works (DOIs), and a version tag.
- Add usage examples: how to load the data with 5–10 lines of code.

3) Link code and data both ways
- In your dataset record: link the GitHub repository and release DOI.
- In your GitHub repo: add `CITATION.cff` and link the dataset DOI in README.

4) Add machine‑readable metadata (simple first)
- Upload a `datapackage.json` or schema files if tabular; include a `README.md` and data dictionary.
- Optional advanced: add a JSON‑LD block for schema.org Dataset on your project website for better indexing.

5) Verify discoverability
- Search your title/keywords; check Google Dataset Search, repository search, and cross‑links.
- Ensure your name/ORCID and affiliations are correct.

Next steps (advanced)
- JSON‑LD Dataset markup: see “Dataset JSON‑LD” for a ready‑to‑adapt block and templates.
- Add DCAT/DCAT‑AP feeds if running a data portal.

Cross‑links: Guided Project Phases 3, 9–10; Deposit & Validation Recipes; Dataset JSON‑LD.
