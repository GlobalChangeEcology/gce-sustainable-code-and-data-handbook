# Git Recipes

Handy commands for non-everyday but useful Git tasks. Read carefully and consider backups when rewriting history.

## Rename the last commit (message only)
```bash
git commit --amend -m "New message"
```

## Combine commits before pushing (interactive rebase)
```bash
git rebase -i HEAD~5
# mark older commits as 'squash' or 'fixup'
```

## Rename a branch
```bash
git branch -m old-name new-name
# push new and delete old on remote
git push -u origin new-name
git push origin --delete old-name
```

## Remove a file from history (filter-repo)
```bash
pip install git-filter-repo
git filter-repo --path secrets.txt --invert-paths
```

## Find the commit that introduced a bug (bisect)
```bash
git bisect start
git bisect bad HEAD
git bisect good <known-good-tag-or-commit>
# run your test at each step, mark good/bad
```

## Submodules (add and update)
```bash
# add
git submodule add https://github.com/org/dep.git external/dep
# init and update
git submodule update --init --recursive
```

## Tagging and releases
```bash
git tag -a v1.2.0 -m "Release v1.2.0"
git push origin v1.2.0
```

## Restore a deleted branch
```bash
git reflog
# find commit, then recreate
git branch restored <commit>
```
