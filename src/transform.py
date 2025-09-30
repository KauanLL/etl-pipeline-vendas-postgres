import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [c.lower() for c in df.columns]

    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
    df["data"] = pd.to_datetime(df["data"], errors="coerce")

    if df["valor"].isnull().any():
        raise ValueError("Valores inválidos encontrados na coluna 'valor'")

    if df["data"].isnull().any():
        raise ValueError("Datas inválidas encontradas na coluna 'data'")

    if (df["valor"] <= 0).any():
        raise ValueError("Foram encontrados valores <= 0 em 'valor'")

    return df
