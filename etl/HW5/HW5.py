# Создать DAG с тремя задачами на PythonOperator: prepare, calculate, report. Нужно использовать: свой Python-декоратор, передачу параметров (op_args/op_kwargs), контекст задачи (**kwargs, ti, execution_date) и XCom.
# 1. Напишите простой декоратор и оберните им функцию одной из задач так, чтобы перед выполнением выводилось сообщение вида «[START] выполняю функцию <имя>», а после — «[END] функция <имя> завершена».
# 2. В задаче prepare функция должна принимать список чисел через op_args (например, [10, 20, 30]) и параметр multiplier через op_kwargs. Из контекста выведите в лог task_id и execution_date. Умножьте каждое число из списка на multiplier, сохраните полученный список в XCom под ключом "numbers_scaled".
# 3. В задаче calculate функция должна прочитать из XCom список "numbers_scaled", посчитать сумму этих чисел, принять параметр username через op_kwargs, сформировать строку вида: User <username>, total sum is <value> и сохранить её в XCom под ключом "summary".
# 4. В задаче report функция должна прочитать из XCom значение "summary" и вывести его в лог как финальный результат.
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[START] выполняю функцию {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[END] функция {func.__name__} завершена")
        return result

    return wrapper


@my_decorator
def prepare_numbers(num, multiplier, **kwargs):
    ti = kwargs["ti"]
    execution_date = kwargs["execution_date"]
    task_id = kwargs["task"].task_id

    print(f"task_id={task_id}, execution_date={execution_date}")

    sc = [n * multiplier for n in num]

    ti.xcom_push(key="numbers_scaled", value=sc)


def calculate_sum(username, **kwargs):
    ti = kwargs["ti"]

    numbers = ti.xcom_pull(key="numbers_scaled", task_ids="prepare")
    total = sum(numbers)
    summary = f"User {username}, total sum is {total}"
    ti.xcom_push(key="summary", value=summary)


def report_result(**kwargs):
    ti = kwargs["ti"]

    summary = ti.xcom_pull(key="summary", task_ids="calculate")
    print(f"Финальный результат: {summary}")


with DAG(
    dag_id="maksim_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
):

    prepare = PythonOperator(
        task_id="prepare",
        python_callable=prepare_numbers,
        op_args=[[10, 20, 30]],
        op_kwargs={"multiplier": 3},
    )

    calculate = PythonOperator(
        task_id="calculate",
        python_callable=calculate_sum,
        op_kwargs={"username": "Maksim"},
    )

    report = PythonOperator(
        task_id="report",
        python_callable=report_result,
    )

    prepare >> calculate >> report
