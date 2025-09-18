# 01 — Policy & Principles

Purpose: Define why we manage data, who is responsible, and the standards we follow.

## Scope
- Applies to all research projects under the Chair of Global Change Ecology (GCE), University of Würzburg.
- Covers data, code, documentation, and derived outputs.

## Roles
- Project Lead: accountable for data quality and compliance.
- Data Steward: owner of this policy, support, training, audits.
- All Staff: follow this manual, maintain metadata, use approved tools.

## Principles
- FAIR: Findable, Accessible, Interoperable, Reusable.
- Good Scientific Practice (DFG): integrity, reproducibility, retention.
- Open by default: publish data/code unless legal/ethical constraints apply.
- Privacy & Ethics: comply with GDPR and ethics approvals for personal/sensitive data.

## Minimum Requirements (Baseline)
- Standard project structure and naming conventions are mandatory.
- Raw data are immutable in `01_RAWDATA/`.
- Every dataset has a `README.md` and data dictionary.
- Git/GitLab for code with protected `main` and releases.
- Backups on university-managed infrastructure.

## Review & Enforcement
- Policy owner: Data Steward.
- Review cadence: every 6 months via Merge Request.
- Non-compliance escalated to Project Lead; remediation plan within 2 weeks.
