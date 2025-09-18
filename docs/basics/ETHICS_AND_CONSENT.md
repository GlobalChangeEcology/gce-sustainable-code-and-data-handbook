---
title: Ethics, Consent, and Anonymisation
---

# Ethics, Consent, and Anonymisation

Use this page to plan ethically sound and legally compliant data sharing from the start.

## Quick Checklist

- Define data categories: personal, sensitive, de‑identified, aggregate.
- Draft consent language that permits data sharing and citation when possible.
- Plan a three‑part strategy: consent, anonymisation, and access control.
- Choose licenses that reflect consent and rights (e.g., CC BY, CC0, ODbL).
- Record rights/ownership and IP for data, code, and documentation.
- Document anonymisation steps in the dataset README and metadata.
- Select a repository with access controls if needed (embargo, restricted).

## Templates and Snippets

Consent language example (for de‑identified sharing):

“I agree that de‑identified data from this study may be shared in a public research repository for reuse. Direct identifiers will be removed, and access to sensitive variables may be restricted. I understand my participation is voluntary and I may withdraw consent as permitted by law.”

Anonymisation notes to include in metadata:

- Direct identifiers removed: names, emails, phone numbers.
- Indirect identifiers generalised: age → age band; location → NUTS2.
- Free‑text reviewed and redacted for unique references.
- Perturbation: date offsets ±k days; top‑coding at threshold X.

## Good Practices

- Start early: align DMP, consent, and repository selection in project setup.
- Balance privacy and utility: remove only what’s necessary; document changes.
- Version control sensitive transformations using pipelines, not ad‑hoc edits.
- Consider differential access: public, restricted, or data use agreements.

## References and Training

- UK Data Service RDM: ethics, consent, anonymisation modules and checklists — https://ukdataservice.ac.uk/learning-hub/research-data-management/
- ICO guidance on effective anonymisation (UK) — https://ico.org.uk/
- The Turing Way — ethics and project design — https://the-turing-way.org/

Cross‑links: Guided Project → Phase 1 (Plan & Setup), Phase 9 (Publish & Cite).

Last updated: 2025‑09‑18
