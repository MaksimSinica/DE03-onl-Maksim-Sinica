import pandas as pd
import numpy as np

df = pd.read_csv("HW8\customers.csv")
df["num_orders"] = np.random.randint(40, 120, size=len(df))  # количество заказов
df["amount_orders"] = np.random.randint(400, 3400, size=len(df))  # сумма заказов
df["age"] = np.random.randint(18, 74, size=len(df))  # Возраст
city = pd.Series(
    [
        "New York",
        "London",
        "Minsk",
        "Moscow",
        "London",
        "Moscow",
        "Minsk",
        "Minsk",
        "Minsk",
        "Moscow",
        "Berlin",
        "Madrid",
        "Mexico City",
        "Moscow",
        "Moscow",
        "Minsk",
        "Singapore",
        "Moscow",
        "Toronto",
        "Berlin",
    ]
)
df["city"] = city  # Город
df["year_registr"] = np.random.randint(2015, 2025, size=len(df))  # Год регистрации
df["avg_check"] = (df["amount_orders"] / df["num_orders"]).round(2)  # Средний чек
print(df)

min_amount = np.min(df["amount_orders"])
print(f"Минимальная сумма заказов: {min_amount}")

sum_amount_orders = df.groupby("city")["amount_orders"].sum()
print(sum_amount_orders)  # Сумма заказов по городам

avg_amount_orders = np.mean(df["amount_orders"])
print(f"Среднняя сумма заказав: {avg_amount_orders}")

filter_age = df[df["age"] > 30]  # Фильтрует покупателей больше 30 лет
print(filter_age)

sort_avg_check = df.sort_values(by="avg_check", ascending=True)
print(sort_avg_check)  # Сортирует по среднему чеку по возрастанию

print(df.iloc[0])  # Выводит первую строку DataFrame
print(df.tail())  # Показывает последние 5 строк

city_minsk = df[df["city"] == "Minsk"]  # Фильтрует товары по городу Минск
print(city_minsk)

srt = city_minsk.sort_values(
    by="year_registr", ascending=False
)  # Сортирует по убыванию по дате регистрации кастомеров с Минска
print(srt)

agregate = df.agg(
    {"num_orders": ["mean", "sum", "min", "max"]}
)  # Выводит среднее, сумму, мин, макс количество заказов
print(agregate)


print(df.describe())  # статистика по числовым столбцам

process_df = df["age"].apply(
    lambda x: x + 10
)  # Применяет функию к Возрасту  +10 к каждому
print(process_df)

renamed = df.rename(columns={"first_name": "NAME"})  # Переименование названия столбца
print(renamed)

drop_col = df.drop(["year_registr"], axis=1)  # Удалили столбец из ДФ
print(drop_col)

print(df.iloc[0:10])  # Выводит первые 10 строк
print(df.loc[15])  # Выводит 15 строку
print(df.shape)  # Показывает размерность ДФ

df.to_csv("HW8\output.csv")  # Запись ДФ в csv файл
