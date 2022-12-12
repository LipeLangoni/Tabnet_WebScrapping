from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import papermill as pm


with DAG('tabnet_workflow', start_date= datetime(2022,12,9), schedule_interval= '@monthly', catchup=False) as dag:

    internacao = pm.execute_notebook(
    "/home/felipe/Documents/tabnet_web_scrapping/crawler_atualizacao.ipynb",
    "/home/felipe/Documents/tabnet_web_scrapping/-{{ execution_date }}.ipynb",
    parameters={"msgs": "Ran from Airflow at {{ execution_date }}!"}
)
    tipo_internacao = pm.execute_notebook(
    "/home/felipe/Documents/tabnet_web_scrapping/crawler_atualizacao_tipo.ipynb",
    "/home/felipe/Documents/tabnet_web_scrapping/-{{ execution_date }}.ipynb",
    parameters={"msgs": "Ran from Airflow at {{ execution_date }}!"}
)

    internacao >> tipo_internacao