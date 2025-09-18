import pandas as pd

df = pd.read_csv("data/example.csv")
summary = df.describe()
summary.to_csv("summary_python.csv", index=True)
print("Wrote summary_python.csv")
