def new_columns(df):  # функция для создания новых колонок
    df["gross"] = df["quantity"] * df["unit_price"]  # новая колонка gross
    df["net"] = (
        df["gross"] * (1 - df["discount"]) + df["shipping_cost"]
    )  # новая колонка net
    df.loc[df["returned"], "net"] = 0  # преобразование net в 0, если товар возвращен
    df["month_order"] = (
        df["order_date"].dt.to_period("M").dt.to_timestamp()
    )  # новая колонка с месяем заказа
