import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame
from pandas.io.common import file_exists
from sqlalchemy import create_engine

def load_data   (df: DataFrame, table_name: str):
    engine = create_engine('postgresql+psycopg2://etl_user:elt_pass@localhost:5432/vendas_db')
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
