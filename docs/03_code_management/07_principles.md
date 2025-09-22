## 3.2 Principles of Good Scientific Code

Scientific code often begins as quick, exploratory scripts. However, without care, such scripts accumulate into a fragile “pile of spaghetti” that only the original author understands.

Key principles for sustainable code include (Wilson et al., 2017):

- **Readability:** Clear, consistent naming and formatting (style guides such as PEP 8 for Python or tidyverse style for R).
- **Modularity:** Break analysis into functions and scripts instead of long monolithic files.
- **Reusability:** Write code that can be adapted or extended.
- **Documentation:** Explain not only what the code does, but also why.

**Example:**

Instead of:

```python
x = [1,2,3,4]; y=[]; 
for i in x: y.append(i*1.2)
```

Better:

```python
def scale_measurements(values, factor=1.2):
    """Scale input values by a given factor."""
    return [v * factor for v in values]

scaled_data = scale_measurements([1, 2, 3, 4])
```

The second version is easier to understand, reuse, and maintain.
