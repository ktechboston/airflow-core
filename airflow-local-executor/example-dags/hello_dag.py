from airflow.models import DAG

from airflow.operators.bash_operator import BashOperator

from datetime import datetime

dag = DAG(dag_id='hello_dag',
          schedule_interval='@daily',
          start_date=datetime(2020, 8, 10))

example_operator = BashOperator(
    task_id='hello_operator',
    bash_command='echo "Today is {{ execution_date }}"',
    dag=dag
)
