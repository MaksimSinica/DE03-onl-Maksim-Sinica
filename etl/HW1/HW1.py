"""У вас есть два CSV-файла: employees_north.csv с сотрудниками северного региона и employees_south.csv с сотрудниками южного региона. Используя Python, прочитайте оба файла и объедините данные в одну таблицу. После объединения нужно очистить данные от сотрудников, у которых нет указанного адреса электронной почты (пустое значение или пропуск). Затем необходимо выделить сотрудников, у которых должность содержит слово “Manager” (без учёта регистра), и сохранить их в отдельный файл managers.csv. Оставшихся сотрудников сохраните в файл regular_staff.csv. Все файлы должны быть сохранены в формате CSV."""

import pandas as pd

df_north = pd.read_csv(r"HW1\employees_north.csv")
df_south = pd.read_csv(r"HW1\employees_south.csv")
df_all = pd.concat([df_north, df_south], ignore_index=True)
print(df_all)
df_dropna = df_all.dropna(subset="email")
# удаляем строки с Nan в майл
print(df_dropna)
df_manager = df_dropna[
    df_dropna["position"].str.contains("Manager", case=False, na=False)
]
# оставляет сотрудников у которых в position присутствует слово Manager
print(df_manager)
df_o = df_dropna[~df_dropna["position"].str.contains("Manager", case=False, na=False)]
# при помощи оператора ~ оставляет всех остальных кто не Manager
print(df_o)
df_manager.to_csv(r"HW1\managers.csv")
df_o.to_csv(r"HW1\regular_staff.csv")
