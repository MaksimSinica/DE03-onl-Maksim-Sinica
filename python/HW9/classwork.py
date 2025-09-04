# Напишите программу на Python, которая загружает данные
# из CSV файла, очищает их (удаляет пропущенные значения
# и дубликаты) и выводит итоговый DataFrame
import pandas as pd

df = pd.read_csv("HW9\data.csv")
print(df)
# df = df.drop_duplicates(subset=["customer_name"])
# df = df.fillna({"product": 0})
# df = df.dropna()
df["total_price"] = df["quantity"] * df["price"]
sort = df[df["product"] == "Mouse"]
print(df)

df["order_date"] = df["order_date"].astype("datetime64[ns]")
# df.info()
# sort_volue = df.sort_values(by="order_date", ascending=False)
# print(sort_volue)
# max_price = df["total_price"].max()
# print(max_price)
# sum_price = df["total_price"].sum()
# print(sum_price)
# exp_price = df[(df["price"] > 300) & (df["price"] < 1000)]
# print(exp_price)
# print(df.loc[1:4])
# print(df.shape)
# print(df.isnull())
# print(df.describe())
# sp = df[df["product"].isna()]
# print(sp)
# gr = (
# df.groupby("product")
# .agg({"price": "sum"})
# .sort_values(by="price", ascending=False)
# .to_csv("file_price_prod.csv")
# )
# print(gr)
p = (
    df[df["quantity"] > 0]
    .groupby("product")
    .agg({"customer_name": pd.Series.nunique})
    .sort_values(by="customer_name", ascending=False)
)
print(p)
Ana = df[df["customer_name"] == "Anna Ivanova"]
print(Ana)
op = df.query('customer_name == "Anna Ivanova"')
print(op)
