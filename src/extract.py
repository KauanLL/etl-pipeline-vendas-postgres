# src/extract.py
from pathlib import Path
import pandas as pd

def extract_data(path: str | None = None) -> pd.DataFrame:

    if path:
        csv_path = Path(path)
    else:
        base = Path(__file__).resolve().parents[1]   # pasta raiz do projeto
        csv_path = base / "data" / "vendas.csv"

    if not csv_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {csv_path}\n(working dir: {Path.cwd()})")

    return pd.read_csv(csv_path)
