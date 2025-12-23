import pandas as pd
from datetime import datetime

# 1️⃣ Read CSV, skip metadata, use Python engine
df = pd.read_csv(
    "data/raw/exoplanets.csv",
    skiprows=294,            # skip the first 294 rows of description
    engine='python',         # Python parser can handle messy lines
    on_bad_lines='skip',     # skip any really broken lines
    dtype=str
)

# 2️⃣ Add ingestion timestamp
df['ingestion_ts'] = datetime.now()

# 3️⃣ Detect numeric columns automatically
numeric_cols = df.columns[df.apply(lambda col: pd.to_numeric(col, errors='coerce').notna().any())]

# 4️⃣ Clean numeric columns
def clean_numeric(val):
    try:
        return round(float(str(val).split('±')[0]), 2)
    except:
        return None

for col in numeric_cols:
    df[col] = df[col].apply(clean_numeric)

# 5️⃣ Save cleaned CSV
df.to_csv("data/raw/exoplanets_cleaned.csv", index=False)

print("Ingestion complete!")
print(df.head())
