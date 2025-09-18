---
title: Biology Exercise — Darwin Core to GBIF via IPT
tags:
  - Exercise
---

# Biology Exercise — Darwin Core to GBIF via IPT

Outcome: publish a small occurrence dataset to GBIF using Darwin Core and IPT.

Prereqs: a CSV with columns: occurrenceID, eventDate, scientificName, decimalLatitude, decimalLongitude, basisOfRecord.

Steps
1) Prepare data (DwC)
- Ensure headers match DwC terms; save as UTF‑8 `occurrence.csv`

2) Package as DwC‑A
- Use the DwC‑A snippet in Biosciences quick‑starts to create `meta.xml` and zip.

3) IPT upload and check
- Create a dataset in your IPT; upload the archive; fix any term/quality warnings; add EML metadata.

4) Publish and verify on GBIF
- Publish from IPT; check the dataset page; verify citations and map.

Links: Domain → Biosciences; Recipes → Deposit & Validation; Reference → Findability & Discovery (Beginner).
