# Minimal Testing Examples

**Python (pytest):**
```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```
Run with: `pytest test_script.py`

**R (testthat):**
```r
add <- function(a, b) a + b
testthat::test_that("add works", {
  testthat::expect_equal(add(2, 3), 5)
})
```
Run with: `testthat::test_file('test_script.R')`
