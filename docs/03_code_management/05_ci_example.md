# Continuous Integration Example (GitHub Actions)

Automate testing on every push with a simple workflow. Save as `.github/workflows/test.yml`:

```yaml
name: Run Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install pytest
      - name: Run tests
        run: pytest
```

For R, see [r-lib/actions](https://github.com/r-lib/actions) for templates.
