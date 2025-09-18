# Team Git Guidelines (Checklist)

Agree on a few conventions to keep collaboration smooth.

## Branch naming
- `feature/<short-topic>` for features
- `fix/<short-topic>` for bug fixes
- `release/<version>` for release prep
- `hotfix/<short-topic>` for urgent fixes

## Commit messages
- Imperative subject (<= 50 chars), optional body (wrap at 72)
- Reference issues/PRs (e.g., "Fix #123")

## Pull requests
- One topic per PR, keep them small
- Require at least one approval and green checks
- Use draft PRs for early feedback

## Protection rules
- Protect `main`: require PR, reviews, status checks
- Disallow force-pushes to `main`
- Require up-to-date branches before merging

## Merging strategy
- Prefer squash merges for feature branches
- Keep `main` linear; rebase your branch before merge

## Releases
- Tag with SemVer (e.g., v1.2.0)
- Update `CHANGELOG.md`; publish GitHub Release notes
- Archive on Zenodo to mint a DOI

## Files & secrets
- Use `.gitignore`, `.gitattributes`, and Git LFS where needed
- Never commit secrets; rotate credentials if exposure is suspected

## Automation
- CI runs tests/docs; required on PRs
- Templates: use PR and Issue templates; CODEOWNERS for reviews
