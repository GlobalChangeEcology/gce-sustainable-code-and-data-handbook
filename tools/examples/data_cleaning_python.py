"""
Minimal Working Example: Data Cleaning in Python
"""
import pandas as pd

data = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': ['x', None, 'y', 'z']
})

# Drop rows with missing values
data_clean = data.dropna()
print("Cleaned Data:\n", data_clean)
