# Practical Guidance: Troubleshooting & Common Pitfalls

---

## Quick Reference Tables

### Essential Git Commands
| Task | Command |
|------|---------|
| Check status | `git status` |
| Add file(s) | `git add <file>` |
| Commit changes | `git commit -m "Message"` |
| See history | `git log` |
| Undo last commit (keep changes) | `git reset --soft HEAD~1` |
| Discard local changes | `git checkout -- <file>` |
| Pull latest changes | `git pull` |
| Push changes | `git push` |

### Essential Conda Commands
| Task | Command |
|------|---------|
| Create new env | `conda create -n myenv python=3.11` |
| Activate env | `conda activate myenv` |
| List envs | `conda env list` |
| Install package | `conda install <package>` |
| Export env | `conda env export > environment.yml` |
| Update conda | `conda update conda` |

### Essential R/renv Commands
| Task | Command |
|------|---------|
| Install package | `install.packages('package')` |
| Install from GitHub | `remotes::install_github('user/repo')` |
| Initialize renv | `renv::init()` |
| Restore env | `renv::restore()` |
| Snapshot env | `renv::snapshot()` |

---

This page provides quick solutions and tips for common problems encountered by researchers using Git, Conda, R, and reproducible workflows. It is especially useful for beginners and non-IT experts.

---


## Step-by-Step Mini-Tutorials

### Resolving a Git Merge Conflict
1. **Try to merge or pull:**
  ```sh
  git pull
  ```
2. **If you see a conflict message:**
  - Open the conflicted file(s). Look for lines like:
    ```
    <<<<<<< HEAD
    Your changes
    =======
    Incoming changes
    >>>>>>> branch-name
    ```
  - Decide which changes to keep. Edit the file to remove the conflict markers and keep only the correct content.
3. **Mark as resolved:**
  ```sh
  git add <file>
  ```
4. **Complete the merge:**
  ```sh
  git commit
  # or, if rebasing:
  git rebase --continue
  ```

### Creating and Using a Conda Environment
1. **Create a new environment:**
  ```sh
  conda create -n myenv python=3.11
  ```
2. **Activate the environment:**
  ```sh
  conda activate myenv
  ```
3. **Install packages:**
  ```sh
  conda install numpy pandas
  ```
4. **Export the environment:**
  ```sh
  conda env export > environment.yml
  ```

### Restoring an R Project with renv
1. **Open your R project directory.**
2. **Restore the environment:**
  ```R
  renv::restore()
  ```
3. **If you get errors about missing packages:**
  - Check your `renv.lock` file for package versions.
  - Try installing missing packages manually:
    ```R
    install.packages('missingpackage')
    ```

---

### Merge Conflicts
- **Problem:** You see a message about a conflict when merging or pulling.
- **Solution:**
  1. Open the conflicted file(s) and look for lines marked with `<<<<<<<`, `=======`, and `>>>>>>>`.
  2. Decide which changes to keep, edit the file, and remove the conflict markers.
  3. Add the resolved file: `git add <file>`
  4. Continue the merge: `git commit` (or `git merge --continue` if rebasing)

### Accidentally Committed the Wrong File
- **Solution:**
  - Undo the last commit but keep changes: `git reset --soft HEAD~1`
  - Remove a file from the last commit: `git rm --cached <file>` then commit again.

### Pushed to the Wrong Branch
- **Solution:**
  - Checkout the correct branch: `git checkout main`
  - Merge or cherry-pick your changes as needed.

---

## Conda & Python Environment Issues

### Package Not Found or Version Error
- **Solution:**
  - Update Conda: `conda update conda`
  - Try a different channel: `conda install -c conda-forge <package>`

### Environment Won’t Activate
- **Solution:**
  - Check you’re in the right directory.
  - Try: `conda init` and restart your terminal.

### Reproducible Environments
- **Tip:** Always export your environment: `conda env export > environment.yml`

---

## R & renv Issues

### Package Installation Fails
- **Solution:**
  - Try installing from CRAN: `install.packages('package')`
  - For GitHub packages: `remotes::install_github('user/repo')`

### renv Not Restoring Environment
- **Solution:**
  - Run `renv::restore()` in your project directory.
  - Check for missing or incompatible package versions in `renv.lock`.

---

## General Workflow Pitfalls

- **Raw data overwritten:** Always keep a backup of original data. Never edit raw files directly.
- **Manual data cleaning:** Use scripts (R, Python) for all data processing steps.
- **Untracked large files:** Use Git LFS or DVC for large datasets.
- **Missing documentation:** Add a README and data dictionary to every project.

---

## Templates & Examples

### Project Template
Start new projects with a ready-made folder structure for data, scripts, and documentation. Download or copy the template from:

`project_template/`

**Structure:**
- `data/` — raw and processed data
- `scripts/` — analysis and processing scripts (R, Python, etc.)
- `docs/` — documentation, reports, and notes

Includes example scripts and environment files for both Python (`environment.yml`) and R (`renv.lock`).

### Minimal Working Examples
Find simple, ready-to-run scripts for common tasks in:

`tools/examples/`

**Examples include:**
- Data cleaning in Python and R
- Plotting in Python and R

All key code/data management examples are provided in both R and Python for accessibility.

---

## Getting Help
- Check the handbook’s FAQ and glossary.
- Search error messages online (Stack Overflow, GitHub Issues, etc.).
- Ask a colleague or your local data steward.

---

*If you encounter a problem not listed here, please suggest an addition to this page!*