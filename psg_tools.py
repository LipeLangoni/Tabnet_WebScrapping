import time
from sqlalchemy import create_engine
import psycopg2
import pandas as pd

def create_connection(user, password, host, db):
    conn_string = 'postgresql://{}:{}@{}/{}'.format(user,password,host,db)
    engine = create_engine(conn_string)
    conn = engine.connect()

def update_keys(var, conn,table, key_table):
    key_value = pd.read_sql_query('select * from {}'.format(key_table),con=conn)
    value = key_value[key_value["Chave" == table]]
    value = value["Valor"]
    if var != value:
        key_value.loc[key_value["Chave"] == table, "Valor"] = var
        key_value.to_sql(key_table, con=conn, if_exists='replace', index=False)
        return True
    else:
        return False
        