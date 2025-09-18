# Advanced

## Rebasing safely
- Rebase your feature branch onto `main` before merging
- Avoid rebasing shared branches that others consume

## Squash vs merge vs rebase-merge
- Squash: clean history; one commit per PR
- Merge: preserve detailed commit history
- Rebase-merge: linear history + individual commits

## Release management
- Annotated tags; signed if possible
- Keep a clean `CHANGELOG.md`; link PRs and issues

## Large files
- Use Git LFS for binaries; avoid committing secrets
