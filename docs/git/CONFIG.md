# Configuration

## Essentials
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.org"
git config --global init.defaultBranch main
git config --global pull.rebase true
```

## Diff and merge tools
```bash
git config --global diff.tool vscode
git config --global difftool.vscode.cmd "code --wait --diff $LOCAL $REMOTE"
```

## Signing (optional)
- Generate a GPG or SSH signing key
- Enable commit signing and upload key to GitHub

## CODEOWNERS & branch protection
- Use CODEOWNERS to auto-request reviews
- Protect `main` with required reviews and checks
