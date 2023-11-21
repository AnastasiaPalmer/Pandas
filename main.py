"""
Візьміть дані про замовлення і покупців і порахуйте:
 1. Скільки замовлень, відправлено першим класом за останні 2 роки?
2. Скільки в базі клієнтів з Каліфорнії?
3. Скільки замовлень вони зробили?
4. Побудуйте зведену таблицю середніх чеків по всіх штатах за кожен рік.
"""

import pandas as pd

# ________________________________________________________________________________________________________________

df_o = pd.read_csv("orders.csv")

first = df_o[(df_o['ship_mode'] == 'First') & (df_o['order_date'] >= '2016-01-01') & (df_o['order_date'] <= '2017-12-31')]
#first['ship_mode'].count()

print(first)

# ________________________________________________________________________________________________________________
df_c = pd.read_csv("customers.csv")

second = df_c[df_c['state'] == 'California']
second['state'].count()

# print(second['id'])

print(df_o[df_o['customer_id'].isin(second['id'])])  # .count()

# ________________________________________________________________________________________________________________

""" Побудуйте зведену таблицю 
                              середніх чеків по всіх штатах за кожен рік. """

dg_n = df_o.join(df_c.set_index('id'), on='customer_id')  # Будуємо зведену таблицю по df_o.id == df_c.customer_id
# print(dg_n)

dg_n['year'] = dg_n['order_date'].str[:4]
print(dg_n)



# Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_rows', None)

# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)

# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)


print(dg_n.groupby(['state', 'year'])['sales'].mean())

