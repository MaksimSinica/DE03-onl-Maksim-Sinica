# Создайте собственный DAG под названием «ваше_имя_homework_dag» со стартовой датой 1 июня 2025 года, без расписания и с ручным запуском. Внутри DAG должны быть следующие задачи:
# 1. Начальная задача, обозначающая старт выполнения.
# 2. Задача на Bash, которая имитирует «загрузку данных», выводя в лог сообщение о том, что вы скачиваете данные (например, «Downloading data…»).
# 3. Задача на Python, в которой функция создаёт список чисел (например, [1, -2, 5, 0, 3]), фильтрует только положительные значения и выводит в лог сумму положительных чисел.
# 4. Задача-сенсор, которая делает паузу около 3 секунд, имитируя ожидание внешнего ресурса.
# 5. Финальная задача, обозначающая окончание DAG.

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.sensors.time_delta import TimeDeltaSensor
from datetime import datetime, timedelta


def sum_pos():
    lst = [1, 5, -4, 0, 3, -8]
    pos = [x for x in lst if x >= 0]
    sum_pos = sum(pos)
    print(f"Сумма положительных числе равна: {sum_pos}")


default_args = {
    "owner": "student",
    "retries": 1,
    "retry_delay": timedelta(seconds=10),
}

with DAG(
    dag_id="Maksim_homework_dag",
    start_date=datetime(2025, 6, 1),
    schedule=None,
    catchup=False,
    default_args=default_args,
) as dag:

    start = EmptyOperator(task_id="start")

    bash_task = BashOperator(
        task_id="bash_example",
        bash_command="echo 'Downloading data…'",
    )

    sums_task = PythonOperator(
        task_id="sum",
        python_callable=sum_pos,
    )

    sensor_task = TimeDeltaSensor(
        task_id="sensor_3_sec",
        delta=timedelta(seconds=3),
        poke_interval=1,
        mode="reschedule",
    )

    end = EmptyOperator(task_id="end")

    start >> bash_task >> sums_task >> sensor_task >> end
