# Workflow

## Daily loop
```bash
git switch -c feature/my-change
git add -p
git commit -m "Add: short message"
git push -u origin feature/my-change
```
Open a PR on GitHub, request review, address comments, and merge.

## Reviews
- Aim for small PRs; leave actionable comments
- Use status checks; require one approval

## Releases
- Tag with SemVer and publish release notes
- Update `CHANGELOG.md`; archive on Zenodo for DOI

## Conflicts
- Pull with rebase; resolve with a visual diff tool
- Re-run tests locally and in CI after resolution
