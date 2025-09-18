# 07 — Sensitive Data

## Definitions & Scope
- Personal data (GDPR), confidential agreements, sensitive locations/species.
- Classify datasets: Public / Internal / Restricted.

## Legal & Ethical Basis
- Ensure lawful basis (consent, contract, public interest) and ethics approvals.
- Data minimisation: collect only what is necessary.

## Protection Measures
- Access control: group-based permissions on NAS/Nextcloud/GitLab.
- Pseudonymisation/anonymisation where feasible; store keys separately.
- Encryption at rest (infrastructure) and in transit (TLS); avoid email attachments.

## Retention & Deletion
- Define retention periods; document in project metadata.
- Secure deletion on request/expiry; record in a deletion log.

## Sharing & Publication
- Remove direct identifiers; evaluate re-identification risk.
- Use controlled-access repositories if needed; specify data use agreements.
