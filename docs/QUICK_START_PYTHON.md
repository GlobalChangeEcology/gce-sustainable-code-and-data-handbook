# Quick Start — Python

Follow these steps to analyze a small CSV reproducibly.

## 1) Environment
```bash
conda create -n gce-quickstart python=3.11 -y
conda activate gce-quickstart
pip install pandas frictionless pandera
```

## 2) Data dictionary
Create `data_dictionary.csv` like:
```
name,type,unit,description,allowed_values,missing_values
id,integer,,Unique identifier,,
value,number,unitless,Example measurement,,
```

## 3) Validate data (optional but recommended)
```python
# validate.py
import pandas as pd
import pandera as pa

schema = pa.DataFrameSchema({
    "id": pa.Column(int),
    "value": pa.Column(float)
})

df = pd.read_csv("03_CLEAN/example.csv")
schema.validate(df)
print("Validation passed")
```

## 4) Reproducible script
```python
# summarize.py
import pandas as pd

df = pd.read_csv("03_CLEAN/example.csv")
summary = df.describe()
summary.to_csv("05_RESULTS/summary.csv")
print("Wrote 05_RESULTS/summary.csv")
```

## 5) Run
```bash
python validate.py
python summarize.py
```

## 6) Next
- Save your environment: `conda env export > environment.yml`
- Commit all changes; push to your repo
- Consider a Snakemake pipeline when steps grow
