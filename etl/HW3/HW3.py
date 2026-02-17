# Создайте DAG под названием «ваше_имя_heavy_task_dag» со стартовой датой 1 января 2024 года, без расписания и с ручным запуском. Внутри должна быть начальная задача, затем задача на Python, которая принимает параметр N, делает задержку примерно 5 секунд, вычисляет сумму чисел от 1 до N и записывает её в лог. Затем должна выполниться завершающая задача.
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta, time


def sum_n(N):
    time.sleep(5)
    sums = sum([x for x in range(1, N + 1)])
    print(f"Сумма чисел равна {sums}")


default_args = {
    "owner": "student",
    "retries": 1,
    "retry_delay": timedelta(seconds=10),
}

with DAG(
    dag_id="Maksim_heavy_task_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    default_args=default_args,
) as dag:

    start = EmptyOperator(task_id="start")

    sm_task = PythonOperator(task_id="sum_n", python_callable=sum_n, op_args=[25])

    end = EmptyOperator(task_id="end")

    start >> sm_task >> end
