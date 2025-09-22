# 2.5 Data Cleaning and Processing

Raw data is rarely ready for analysis. Errors, inconsistencies, and missing values often need to be addressed. However, how cleaning is done makes a huge difference.

Manual edits in Excel may seem convenient, but they are irreproducible — no one can retrace the exact steps taken. Instead, cleaning should be done with scripts (in R, Python, etc.) that record every transformation. This way, the cleaning process can be repeated, checked, and adapted as needed (Sandve et al., 2013).

**Example:**

- **Bad practice:** Deleting outliers by hand in Excel.
- **Good practice:** Writing a script that filters out values beyond a threshold, with comments explaining the rationale.
