## 4.3 Dependency Management

Modern research often relies on dozens of external packages and libraries. Keeping track of these dependencies is essential.

- In Python: use `requirements.txt` or `environment.yml` files with Conda to record package versions.
- In R: use `renv` or `packrat` to snapshot dependencies.
- Cross-platform: use `pip freeze` or containerization tools.

Explicitly recording dependencies allows others to recreate the same software setup. Without this, code may break in unpredictable ways (Wilson et al., 2017).
