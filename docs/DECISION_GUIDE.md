# Decision Guide

Use this flow to pick tools and repositories.

```mermaid
flowchart TD
  A[Start] --> B{Primary need?}
  B -->|Analyze data| C{Preferred language?}
  C -->|Python| C1[Python env (Conda/Poetry) + Pandas]
  C -->|R| C2[R env (renv) + tidyverse]
  B -->|Automate pipeline| D{Size/cluster?}
  D -->|Small/Local| D1[Snakemake]
  D -->|Large/HPC| D2[Nextflow]
  B -->|Publish dataset| E{Discipline?}
  E -->|Environmental/Earth| E1[PANGAEA]
  E -->|Biodiversity| E2[GBIF]
  E -->|General| E3[Zenodo]
  B -->|Code & results website| F[MkDocs + GitHub Pages]
  C1 --> G[Add validation: pandera]
  C2 --> H[Add validation: pointblank]
  D1 --> I[Capture envs per rule]
  D2 --> J[Containers + profiles]
  E1 --> K[Prepare README + dictionary]
  E2 --> K
  E3 --> K
```
