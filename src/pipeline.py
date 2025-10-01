from prefect import  flow, task, get_run_logger
import pandas as pd
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

@task
def extrack_task(path: str):
    logger = get_run_logger()
    logger.info(f'Lendo arquivo CSV de {path}')
    return extract_data(path)

@task
def transform_task(df: pd.DataFrame):
    logger = get_run_logger()
    logger.info(f'Iniciando Transformação e validação de dados')
    return transform_data(df)

@task
def load_task(df: pd.DataFrame, table_name: str):
    logger = get_run_logger()
    logger.info(f'Carregando dados na tabela {table_name}')
    return load_data(df, table_name)

@flow
def etl_pipeline(path: str, table_name: str):
    df = extrack_task(path)
    df = transform_task(df)
    load_task(df, table_name)

if __name__ == "__main__":
    from pathlib import Path
    base = Path(__file__).resolve().parents[1]
    default_path = base / "data" / "vendas.csv"
    etl_pipeline(str(default_path), "vendas")