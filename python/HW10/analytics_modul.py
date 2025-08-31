def analytics(df):  # функция для аналитики
    def sum_gross_net():  # функция для подсчета суммы заказов
        sum_gross = df["gross"].sum().round(2)
        sum_net = df["net"].sum().round(2)
        return sum_gross, sum_net

    def avg_median_net():  # функция для подсчета среднего и медианного значения выручки
        avg = df["net"].mean().round(2)
        median = df["net"].median().round(2)
        return avg, median

    def unique_customers():  # функция для подсчета уникальных клиентов
        unique_cust = df["customer_id"].nunique()
        return unique_cust

    def returned_orders():  # функция для подсчета количества возвратов
        returned = df["returned"].sum()
        return returned

    def top_n_products():  # функция для подсчета топ N продуктов по выручке
        top_products = (
            df.groupby("product")["net"].sum().sort_values(ascending=False).head(5)
        )
        return top_products

    def count_orders_country():
        count_orders = (
            df.groupby("country")["order_id"].nunique().sort_values(ascending=False)
        )
        sum_net_country = (
            df.groupby("country")["net"].sum().round(2).sort_values(ascending=False)
        )
        return count_orders, sum_net_country

    def month_orders_count():
        month_orders = df.groupby("month_order")["order_id"].nunique()
        return month_orders

    sum_gross, sum_net = sum_gross_net()
    avg, median = avg_median_net()
    unique_cust = unique_customers()
    returned = returned_orders()
    top_products = top_n_products()
    count_orders, sum_net_country = count_orders_country()
    month_orders = month_orders_count()

    return (
        sum_gross,
        sum_net,
        avg,
        median,
        unique_cust,
        returned,
        top_products,
        count_orders,
        sum_net_country,
        month_orders,
    )
