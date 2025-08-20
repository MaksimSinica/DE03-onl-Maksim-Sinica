import pandas as pd
import numpy as np

# • Загрузите данные из CSV файла
# • Выполните основные операции с данными: фильтрация,
# сортировка, агрегация с использованием pandas
# • Применить numpy для числовых вычислений
df = pd.read_csv(r"sales.csv")
prices = [10.99, 20.50, 15.75, 30.00, 25.00, 18.25, 22.10]
count = [56, 24, 12, 5, 6, 23, 4]
df["count"] = count
df["price"] = prices
df["total_price"] = df["price"] * df["count"]
print(df)
low_count = df[df["count"] < 12]
print(low_count)
sorted = df.sort_values(by="total_price", ascending=False)
print(sorted)
max_total_price = df.groupby("category")["total_price"].max()
print(max_total_price)
avr_total_price = np.mean(df["total_price"])
print(avr_total_price)
value = np.median(df["total_price"])
print(value)
