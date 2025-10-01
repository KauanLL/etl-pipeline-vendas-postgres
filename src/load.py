import pandas as pd
from sqlalchemy import create_engine

def load_data(df: pd.DataFrame, table_name: str):
    engine = create_engine('postgresql+psycopg2://etl_user:etl_pass@localhost:5432/vendas_db')
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
