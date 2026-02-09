# Создайте DAG под названием «ваше_имя_positive_count_dag» со стартовой датой 1 января 2024 года и без расписания.
# В DAG должна быть одна задача на Python, которая создаёт список чисел [-5, -2, 0, 3, 7, 10, -1, 4], считает, сколько среди них положительных, и выводит в лог сообщение вида «Количество положительных чисел: X».
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta


def positive():
    lst = [-5, -2, 0, 3, 7, 10, -1, 4]
    cnt = len([x for x in lst if x >= 0])
    print(f"Количество положительных чисел: {cnt}")


default_args = {
    "owner": "student",
    "retries": 1,
    "retry_delay": timedelta(seconds=10),
}

with DAG(
    dag_id="Maksim_positive_count_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    default_args=default_args,
) as dag:

    start = EmptyOperator(task_id="start")

    cnt_task = PythonOperator(
        task_id="count_posit",
        python_callable=positive,
    )

    end = EmptyOperator(task_id="end")

    start >> cnt_task >> end
