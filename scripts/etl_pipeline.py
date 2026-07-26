import os
import pandas as pd
from sqlalchemy import create_engine

# 1. Database Connection Configuration
# Replace 'your_password' with the master password you set up for PostgreSQL
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/ai_sentiment_db"
engine = create_engine(DATABASE_URL)

def clean_and_load_data():
    print("🚀 Starting ETL pipeline...")
    
    # Define file paths (Adjust these to match where you saved your downloaded CSVs)
    path_2024 = "../data/raw_2024/survey_results_public_2024.csv"
    path_2025 = "../data/raw_2025/survey_results_public_2025.csv"
    
    # --- PROCESSING 2024 DATA ---
    if os.path.exists(path_2024):
        print("📊 Processing 2024 survey data...")
        df_2024 = pd.read_csv(path_2024, low_memory=False)
        
        # Select target columns for analysis
        cols_2024 = ['ResponseId', 'MainBranch', 'Age', 'YearsCodePro', 'AISelect', 'AISent', 'AIAcc']
        # Ensure they exist in the file
        cols_to_keep = [c for c in cols_2024 if c in df_2024.columns]
        df_clean_2024 = df_2024[cols_to_keep].copy()
        
        # Standardize and clean schemas
        df_clean_2024['survey_year'] = 2024
        df_clean_2024['YearsCodePro'] = pd.to_numeric(df_clean_2024['YearsCodePro'].str.replace('Less than 1 year', '0').str.replace('More than 50 years', '51'), errors='coerce')
        
        # Load into PostgreSQL
        df_clean_2024.to_sql('raw_survey_data', engine, if_exists='append', index=False)
        print("✅ 2024 data successfully appended to PostgreSQL database.")
    else:
        print(f"⚠️ Warning: 2024 file not found at {path_2024}")

    # --- PROCESSING 2025 DATA ---
    if os.path.exists(path_2025):
        if os.path.exists(path_2025):
            print("📊 Processing 2025 survey data...")
            df_2025 = pd.read_csv(path_2025, low_memory=False)
        
        # 1. NEW FALLBACK CODE GOES HERE: Check and handle Schema Drift for YearsCodePro
        actual_col_name = None
        for col in df_2025.columns:
            if col.lower() == 'yearscodepro':
                actual_col_name = col
                break
        
        if actual_col_name:
            df_2025 = df_2025.rename(columns={actual_col_name: 'YearsCodePro'})
            print(f"🔄 Automatically mapped 2025 column '{actual_col_name}' to 'YearsCodePro'")
        elif 'YearsCode' in df_2025.columns:
            # If professional years column is missing entirely, fallback to overall coding years
            df_2025 = df_2025.rename(columns={'YearsCode': 'YearsCodePro'})
            print("🔄 'YearsCodePro' missing. Automatically falling back to 'YearsCode' for experience metrics.")

        # Define columns we want
        cols_2025 = ['ResponseId', 'MainBranch', 'Age', 'YearsCodePro', 'AISelect', 'AISent', 'AIAcc']
        cols_to_keep_25 = [c for c in cols_2025 if c in df_2025.columns]
        df_clean_2025 = df_2025[cols_to_keep_25].copy()
        
        df_clean_2025['survey_year'] = 2025
        
        # ONLY clean 'YearsCodePro' if it was successfully found in the dataset!
        if 'YearsCodePro' in df_clean_2025.columns:
            df_clean_2025['YearsCodePro'] = pd.to_numeric(
                df_clean_2025['YearsCodePro'].astype(str)
                                             .str.replace('Less than 1 year', '0', case=False)
                                             .str.replace('More than 50 years', '51', case=False), 
                errors='coerce'
            )
        else:
            print("⚠️ Warning: 'YearsCodePro' completely missing from 2025 columns list!")
            df_clean_2025['YearsCodePro'] = None # Fill with empty column so it doesn't break table structures
        
        # Append into the database
        df_clean_2025.to_sql('raw_survey_data', engine, if_exists='append', index=False)
        print("✅ 2025 data successfully handled and appended.")

    print("🏁 Pipeline run complete!")

if __name__ == "__main__":
    clean_and_load_data()