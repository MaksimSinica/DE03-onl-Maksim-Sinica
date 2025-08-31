from load_modul import load_orders
from preparation_modul import new_columns
from analytics_modul import analytics
from save_modul import save_report_1

try:
    df = load_orders()
    new_columns(df)
    (
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
    ) = analytics(df)
    save_report_1(
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
except FileNotFoundError:
    print("Файл не найден!")
except PermissionError:
    print("Нет доступа к файлу!")
except IsADirectoryError:
    print("Указан путь к папке, а не к файлу!")
except IOError:
    print("Ошибка ввода-вывода файла!")
except UnicodeDecodeError:
    print("Неправильная кодировка файла!")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")
