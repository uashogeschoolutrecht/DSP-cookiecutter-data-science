from datetime import datetime, timedelta
import requests
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import logging

# Define the default_args dictionary
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Define the DAG
dag = DAG(
    'example_api_call',
    default_args=default_args,
    description='A simple API call DAG',
    schedule_interval=timedelta(minutes=1),
)

# Define the Python function to call the API
def fetch_api_data():
    url = 'https://official-joke-api.appspot.com/jokes/random'  # Official Joke API URL
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        logging.info("API response data: %s", data)
        
    except requests.exceptions.RequestException as e:
        logging.error("API request failed: %s", e)

# Define the PythonOperator to execute the function
api_call_task = PythonOperator(
    task_id='fetch_api_data',
    python_callable=fetch_api_data,
    dag=dag,
)

# Define the task dependencies
api_call_task
