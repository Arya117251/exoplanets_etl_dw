import pandas as pd
import os

def create_dimension_and_fact_tables(input_csv, warehouse_folder="Warehouse"):
    # Make sure warehouse folder exists
    os.makedirs(warehouse_folder, exist_ok=True)
    
    # Load CSV safely
    df = pd.read_csv(input_csv, low_memory=False)
    
    # ------------------------
    # 1. Planet Dimension Table
    # ------------------------
    planet_dim = df[['rowid', 'pl_name', 'pl_letter', 'hd_name',
                     'hostname', 'discoverymethod', 'disc_year']].drop_duplicates()
    planet_dim = planet_dim.reset_index(drop=True)
    planet_dim['planet_id'] = planet_dim.index + 1  # PK
    planet_dim.to_csv(os.path.join(warehouse_folder, "planet_dim.csv"), index=False)

    # ------------------------
    # 2. Star Dimension Table
    # ------------------------
    star_dim = df[['st_refname', 'st_spectype', 'st_mass', 'st_rad',
                   'st_age', 'st_teff']].drop_duplicates()
    star_dim = star_dim.reset_index(drop=True)
    star_dim['star_id'] = star_dim.index + 1  # PK
    star_dim.to_csv(os.path.join(warehouse_folder, "star_dim.csv"), index=False)

    # ------------------------
    # 3. System Dimension Table
    # ------------------------
    system_dim = df[['sy_snum', 'sy_pnum', 'sy_mnum',
                     'hostname', 'sy_dist', 'sy_plx']].drop_duplicates()
    system_dim = system_dim.reset_index(drop=True)
    system_dim['system_id'] = system_dim.index + 1
    system_dim.to_csv(os.path.join(warehouse_folder, "system_dim.csv"), index=False)

    # ------------------------
    # 4. Fact Table (memory-safe)
    # ------------------------
    fact = df[['rowid', 'pl_name', 'st_refname', 'hostname',
               'pl_orbper', 'pl_rade', 'pl_masse']]

    # Build lookup dictionaries
    planet_lookup = dict(zip(planet_dim['pl_name'], planet_dim['planet_id']))
    star_lookup = dict(zip(star_dim['st_refname'], star_dim['star_id']))
    system_lookup = dict(zip(system_dim['hostname'], system_dim['system_id']))

    # Map foreign keys (NO MERGES, memory-friendly)
    fact['planet_id'] = fact['pl_name'].map(planet_lookup)
    fact['star_id'] = fact['st_refname'].map(star_lookup)
    fact['system_id'] = fact['hostname'].map(system_lookup)

    fact = fact[['rowid', 'planet_id', 'star_id',
                 'system_id', 'pl_orbper', 'pl_rade', 'pl_masse']]

    fact.to_csv(os.path.join(warehouse_folder, "exoplanet_fact.csv"), index=False)

    print("DW tables created in:", warehouse_folder)


if __name__ == "__main__":
    input_csv_path = r"..\data\raw\exoplanets_cleaned.csv"
    print("Using CSV:", os.path.abspath(input_csv_path))
    create_dimension_and_fact_tables(input_csv_path)
