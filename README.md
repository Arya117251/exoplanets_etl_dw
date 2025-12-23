# # 🌌 Exoplanet Data Vault: ETL & Visualization Ready

## 🚀 Project Overview
This project builds a **mini Data Warehouse (DW)** for exoplanet and star system data.  
We take raw CSV data, clean and transform it, and load it into structured DW tables for analysis and future predictions.  

The goal: **From raw data → Dimension & Fact Tables → Ready for Analysis/ML**.

---

## 📁 Project Structure (Local / Planned GitHub)

exoplanets_etl_dw/
│
├── data/ # Optional raw CSVs
├── ingestion/
│ └── ingest_exoplanets.py # Load & preprocess CSV
├── orchestration/
│ ├── create_dw_tables.py # Create DW tables
│ └── check_tables.py # Inspect DW tables
├── Warehouse/
│ ├── exoplanet_fact.csv
│ ├── planet_dim.csv
│ ├── star_dim.csv
│ └── system_dim.csv
└── README.md


---

## 🛠️ What We've Done So Far

### 1️⃣ Data Ingestion
- Loaded raw CSV data of exoplanets.  
- Cleaned it into a usable format (`exoplanets_cleaned.csv`).  
- Script: `ingest_exoplanets.py` ✅

### 2️⃣ Dimension Tables
- **Planet Dimension (`planet_dim.csv`)**: Unique planets with `planet_id`. 🌍  
- **Star Dimension (`star_dim.csv`)**: Unique stars with `star_id`. ⭐  
- **System Dimension (`system_dim.csv`)**: Star system info with `system_id`. 🪐  

### 3️⃣ Fact Table
- **Exoplanet Fact (`exoplanet_fact.csv`)**: Links planets, stars, and systems using foreign keys. 🔗  
- Stores key planetary metrics like `pl_orbper`, `pl_rade`, `pl_masse`. 📊  

### 4️⃣ Orchestration & DW Creation
- Automated table creation with `create_dw_tables.py`. ⚙️  
- Memory-efficient mapping avoids large merge operations. 💾  
- `check_tables.py` lets us preview DW tables quickly (`head()`). 👀  

### 5️⃣ Warehouse Storage
- All CSVs are stored in `Warehouse/`. 📂  
- Ready for further **analysis, visualization, or predictive modeling**. 🎯

---

## 🔮 Next Steps (Future)
- Add Jupyter Notebook for visualizations 📈  
- Explore ML: predict planet mass/radius, classify discovery methods 🤖  
- Add dashboards using free tools (Python/Matplotlib, Power BI Desktop) 📊  
- Possibly move DW to SQLite/PostgreSQL for proper DB setup 🗄️  
