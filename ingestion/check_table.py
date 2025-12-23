import pandas as pd
import os

base_path = r"C:\Users\Hp\warehouse"

# List of all CSVs
csv_files = ["planet_dim.csv", "star_dim.csv", "system_dim.csv", "exoplanet_fact.csv"]

for csv_file in csv_files:
    path = os.path.join(base_path, csv_file)
    print(f"--- Head of {csv_file} ---")
    df = pd.read_csv(path, low_memory=False)
    print(df.head(), "\n")
