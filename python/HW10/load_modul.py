from errors_modul import LoadError, load_data
import pandas as pd


def load_orders():
    try:
        df = pd.read_csv("HW10\orders1.csv")
    except FileNotFoundError:
        print("Файл не найден")
    print(df.info())  # проверка типов данных
    df["order_date"] = df["order_date"].astype(
        "datetime64[ns]"
    )  # испрвление типа данных в дате
    try:  # проверка цены, скидки, количества на ошибки в модуле errors_modul
        load_data(df)
    except LoadError as e:
        print(f"Ошибка в данных: {e}")
    else:
        print("Данные успешно проверены")
    return df
