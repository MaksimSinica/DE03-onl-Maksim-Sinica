# Создайте программу, которая загружает данные из REST API, выполняет предварительную
# обработку данных (удаление пропущенных значений, преобразование
# типов), и сохраняет очищенные данные в новый CSV файл.
import requests
import pandas as pd

response = requests.get("https://fakestoreapi.com/products")

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)

else:
    print(f"Failed to retrieve data: {response.status_code}")

df_rating = df["rating"].apply(pd.Series)  # Разделим словарь на два новых толбца
df = pd.concat(
    [df.drop(columns=["rating"]), df_rating], axis=1
)  # Добавим эти колонки обратно в ДФ

Non = df.isna().sum()  # Проверяем есть ли в колонках нулевые значения
print(Non)
print(df.dtypes)
df["count"] = df["count"].astype("int32")  # Преобразуем тип данных в колонке count

df = df.drop("image", axis=1)  # Удаляем колонку с картинками
df = df.drop_duplicates()  # Удаляем дубликаты
print(df)
df.to_csv(
    r"HW9\clean_data.csv", index=False
)  # Сохраняем промежуточный результат в новый CSV файл

df2 = (
    df.groupby("category")
    .agg({"price": "mean", "rate": "mean", "count": "sum"})
    .round(2)
    .rename(columns={"price": "avg_price", "rate": "avg_rate", "count": "total_count"})
)
print(df2)
# группируем по категории и находим среднее значение цены, рейтинга и сумму по количеству отзывов покупателей
df2.to_csv(r"HW9\agg_data.csv", index=True)  # Сохраняем в новый CSV файл

# =================================================================================================================
""" avg_price = df["price"].mean()
print(f"Средняя цена всех товаров: {avg_price.round(2)}")

max_rate = df["rate"].max()
print(f"Максимальный рейтинг товара: {max_rate}")

title = df[df["rate"] == max_rate]["title"]
print(f"Товары с максимальным рейтингом: {title}")

avg_price_cat = df.groupby("category").agg({"price": "mean"})
print(f"Средняя цена товаров по категориям: \n {avg_price_cat.round(2)}")

max_rate_cat = df.groupby("category").agg({"rate": "max"})
print(f"Максимальный рейтинг товаров по категориям: \n {max_rate_cat}")

top = df.sort_values(by="rate", ascending=False).head(5)
print(f"Топ 5 товаров по рейтингу: \n {top[['title', 'rate']]}")

product_agg = df[(df["rate"] >= 4.5) & (df["count"] >= 100)]
print(
    f"Товары с рейтингом выше 4.5 и количеством отзывов больше 100: \n {product_agg[['title', 'rate', 'count']]}"
)
max_price = df.groupby("category").max("price")
print(f"Самый дорогой товар в каждой категории: \n {max_price}")

avg_price_10 = df.sort_values(by="count", ascending=False).head(10)
print(
    f"Средняя цена 10 самых популярных товаров: {avg_price_10['price'].mean().round(2)}"
)

top5 = df.sort_values(by=("description"), ascending=False).head(5)
print(f"Топ 5 товаров с самыми длинными описаниями: \n {top5[['id', 'description']]}") """
