# Git Commands for Researchers - Quick Reference

*Print this page for your desk reference | [Download PDF](git_commands_cheatsheet.pdf)*

## Essential Daily Commands

### Starting a Project
```bash
git init                    # Initialize new repository
git clone [url]             # Copy existing repository
git config --global user.name "Your Name"
git config --global user.email "you@email.com"
```

### Saving Your Work
```bash
git status                  # Check what's changed
git add file.txt            # Stage specific file
git add .                   # Stage all changes
git commit -m "Description" # Save snapshot with message
```

### Working with Remote Repositories
```bash
git remote add origin [url] # Connect to GitHub/GitLab
git push origin main        # Upload your changes
git pull origin main        # Download latest changes
git fetch                   # Check for updates (safe)
```

## Branch Management
```bash
git branch                  # List branches
git branch new-feature      # Create new branch
git checkout new-feature    # Switch to branch
git checkout -b new-feature # Create and switch
git merge new-feature       # Merge branch into current
git branch -d new-feature   # Delete merged branch
```

## Viewing History
```bash
git log --oneline           # Compact history
git log --graph             # Visual branch history
git diff                    # Show current changes
git diff --staged           # Show staged changes
git show [commit-id]        # Show specific commit
```

## Fixing Mistakes

### Before Committing
```bash
git restore file.txt        # Undo changes to file
git restore --staged file.txt # Unstage file
git stash                   # Temporarily save changes
git stash pop               # Restore stashed changes
```

### After Committing
```bash
git reset --soft HEAD~1     # Undo last commit, keep changes
git reset --hard HEAD~1     # Undo last commit, discard changes
git revert [commit-id]      # Safely undo old commit
```

## Large Files & Data
```bash
git lfs track "*.csv"       # Track large files with LFS
git lfs ls-files            # List tracked large files
git lfs pull                # Download large files
```

## Collaboration
```bash
git blame file.txt          # See who changed each line
git log --author="Name"     # Filter commits by author
git cherry-pick [commit-id] # Copy commit from another branch
```

## Quick Fixes for Common Problems

| Problem | Solution |
|---------|----------|
| "I added the wrong file" | `git restore --staged filename` |
| "I want to undo my last commit" | `git reset --soft HEAD~1` |
| "I'm on the wrong branch" | `git checkout correct-branch` |
| "I have merge conflicts" | Edit files, then `git add .` and `git commit` |
| "I forgot to add files to my commit" | `git add missed-file` then `git commit --amend` |
| "I want to see what changed" | `git diff` or `git status` |

## Best Practices for Researchers

✅ **DO:**
- Commit often with clear messages
- Use branches for experiments
- Pull before pushing
- Keep data and code separate
- Write meaningful commit messages

❌ **DON'T:**
- Commit large binary files (use LFS)
- Work directly on main branch
- Commit broken code
- Use vague commit messages
- Store passwords in repositories

## Commit Message Templates

**Good examples:**
- `Add data cleaning script for soil samples`
- `Fix bug in temperature conversion function`
- `Update README with installation instructions`
- `Remove deprecated analysis functions`

**Bad examples:**
- `stuff`
- `fixed it`
- `final version`
- `asdf`

## Emergency Commands

### "I broke everything!"
```bash
git reflog                  # Find lost commits
git reset --hard [commit-id] # Go back to working state
```

### "I need help!"
```bash
git status                  # Always start here
git log --oneline -10       # See recent history
git remote -v               # Check remote connections
```

## Configuration Tips

### One-time setup
```bash
# Better log format
git config --global alias.lg "log --oneline --graph --all"

# Default editor
git config --global core.editor "code --wait"  # VS Code
git config --global core.editor "nano"         # Nano

# Ignore case sensitivity issues
git config --global core.ignorecase false
```

### Useful aliases
```bash
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
```

---

**Remember:** When in doubt, run `git status` first! It tells you exactly what Git is thinking.

**Need more help?** 
- [Official Git documentation](https://git-scm.com/docs)
- [GitHub's Git handbook](https://guides.github.com/introduction/git-handbook/)
- [Interactive Git tutorial](https://learngitbranching.js.org/)

*This cheat sheet covers 90% of daily Git usage for researchers. Print it, laminate it, love it!*