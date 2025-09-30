import pandas as pd
from pathlib import Path

def extract_data():
    raw_path = Path("../data/raw/")
    all_files = list(raw_path.glob("*.csv"))
    df_list = [pd.read_csv(f) for f in all_files]
    df = pd.concat(df_list, ignore_index=True)
    return df