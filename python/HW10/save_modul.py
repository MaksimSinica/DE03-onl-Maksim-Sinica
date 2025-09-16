import pandas as pd


# Создаем новые датафреймы с данными анализа и сохраняем их в csv файлы.
def save_report_1(
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
):
    try:
        df1 = pd.DataFrame(
            [
                {
                    "Общая сумма заказов": sum_gross,
                    "Общая сумма заказов с учетом скидок и возвратов, доставки": sum_net,
                    "Среднее значение выручки": avg,
                    "Медианное значение выручки": median,
                    "Количество уникальных клиентов": unique_cust,
                    "Количество возвратов": returned,
                }
            ]
        )
        df1.to_csv("HW10/report_overview.csv", index=False)

        df2 = pd.DataFrame([{"Топ 5 продуктов по выручке": top_products}])
        df2.to_csv("HW10/report_top_products.csv", index=False)

        df3 = pd.DataFrame(
            [
                {
                    "Количество заказов по странам": count_orders,
                    "Сумма выручки по странам": sum_net_country,
                }
            ]
        )
        df3.to_csv("HW10/report_countries.csv", index=False)

        df4 = pd.DataFrame([{"Количество заказов по месяцам": month_orders}])
        df4.to_csv("HW10/report_monthly.csv", index=False)
        print("Отчеты успешно сохранены")
    except Exception as e:
        print(f"Ошибка при сохранении отчетов: {e}")
    except PermissionError:
        print("Нет прав на запись в один из  файлов")
