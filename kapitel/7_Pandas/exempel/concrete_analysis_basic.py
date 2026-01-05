# concrete_analysis_basic.py

"""
Basic analysis of UCI Concrete Compressive Strength dataset.
Demonstrates:
- Downloading dataset
- Grouping and aggregation
- Simple plotting
- Excel export
"""

import pandas as pd
import matplotlib.pyplot as plt
import requests
import os, sys

# ----------------------------
# 1. Download and load dataset
# ----------------------------
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/concrete/compressive/Concrete_Data.xls"

# URL of the .xls file
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/concrete/compressive/Concrete_Data.xls"
local_filename = "Concrete_Data.xls"

# Download using requests
response = requests.get(url)
with open(local_filename, "wb") as f:
    f.write(response.content)

os.system("in2csv Concrete_Data.xls > Concrete_Data.csv")

df = pd.read_csv("Concrete_Data.csv")

# Optional: Clean column names


df.columns = [c.strip().lower().split("(")[0].replace(" ", "_").rstrip("_") for c in df.columns]
print("Dataset loaded with shape:", df.shape)
print("Columns:", df.columns)


# ----------------------------
# 2. Group and aggregate
# ----------------------------
strength_by_age = df.groupby("age")[["concrete_compressive_strength"]].mean()

# ----------------------------
# 3. Plot strength vs. cement and water
# ----------------------------
plt.figure(figsize=(10, 5))
plt.scatter(df["cement"], df["concrete_compressive_strength"], alpha=0.5, label="Cement")
plt.scatter(df["water"], df["concrete_compressive_strength"], alpha=0.5, label="Water")
plt.xlabel("Content (kg/m³)")
plt.ylabel("Compressive Strength (MPa)")
plt.title("Concrete Strength vs. Cement and Water Content")
plt.legend()
plt.tight_layout()
plt.savefig("strength_vs_material.png")
plt.show()

# ----------------------------
# 4. Export to Excel
# ----------------------------
with pd.ExcelWriter("concrete_summary.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Raw Data", index=False)
    strength_by_age.to_excel(writer, sheet_name="Mean Strength by Age")