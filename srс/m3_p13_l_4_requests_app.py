import psycopg2
# from psycopg.extras import execute_batch
from psycopg2.extras import execute_values

conn = psycopg2.connect('postgresql://tirion:secret@localhost:5432/tirion')

# BEGIN (write your solution here)


def batch_insert(conn_, products_):
    with conn_.cursor() as curs:
        values = [(product['name'], product['price'], product['quantity'])
                  for product in products_]
        execute_values(
            curs,
            "INSERT INTO products (name, price, quantity) VALUES %s",
            values
        )
        conn.commit()


def get_all_products(conn_):
    with conn_.cursor() as curs:
        curs.execute("SELECT * FROM products ORDER BY price desc;",)
        result_ = list(curs.fetchall())
        conn.commit()
    return result_

# END


products = [
    {'name': 'milk', 'price': 12, 'quantity': 20},
    {'name': 'bread', 'price': 3, 'quantity': 10},
    {'name': 'orange', 'price': 6, 'quantity': 5}
]

result = get_all_products(conn)  # []
print(result)

batch_insert(conn, products)

result = get_all_products(conn)  # []
print(result)

# !src / solution.py
# *Создайте функцию, batch_insert(), которая принимает соединение,
# *и список товаров и массово добавляет их в базу. Каждый товар представлен
# *словарем с ключами name, price, и quantity. Для безопасной и быстрой
# *работы с базой данных используйте плейсхолдеры.

# *Так же создайте функцию get_all_products(), которая принимает соединение,
# *и возвращает весь список товаров, отсортированый по цене товара DESC.

# ?CREATE TABLE products(
# ?    id SERIAL PRIMARY KEY,
# ?    name VARCHAR(255) NOT NULL,
# ?    price NUMERIC NOT NULL,
# ?    quantity INT NOT NULL
# ?)

# conn = psycopg2.connect('..')

# products = [
#     {'name': 'milk', 'price': 12, 'quantity': 20},
#     {'name': 'bread', 'price': 3, 'quantity': 10},
#     {'name': 'orange', 'price': 6, 'quantity': 5}
# ]
# get_all_products(conn)  # []

# batch_insert(conn, products)
# get_all_products(conn)
# # [(1, 'milk', 12, 20),
# #  (3, 'orange', 6, 5),
# #  (2, 'bread', 3, 10)]
# !Подсказки
# *Для массовой вставки в БД используется функция execute_values

# !решение ментора
# ?# BEGIN
# *def batch_insert(conn, products):
#     with conn.cursor() as cur:
#         values = [(p['name'], p['price'], p['quantity']) for p in products]

#        insert_query = "INSERT INTO products (name, price, quantity) VALUES %s"

#         execute_values(cur, insert_query, values)
#     conn.commit()


# *def get_all_products(conn):
#     with conn.cursor() as cur:
#         sql = "SELECT * FROM products ORDER BY price DESC;"
#         cur.execute(sql)
#         result = cur.fetchall()
#     conn.commit()
#     return result
# ?# END


# !тут по теории урока

# brand = "Renault"
# model = "Megan 3"


# with conn.cursor() as curs:
#     # также можно использовать именованные аргументы
#     curs.execute(
#         "INSERT INTO cars (brand, model) VALUES (%(brand)s, %(model)s);", {
#             'model': model,
#             'brand': brand
#         }
#     )
#     conn.commit()
#     print(curs.rowcount)

# with conn.cursor() as curs:
#     # для позиционных аргументов всегда передается последовательность,
#     # даже если параметр один
#     # здесь передается кортеж (name,)
#     curs.execute("SELECT id, brand FROM cars WHERE brand=%s;", (brand,))
#     print(curs.fetchall())

# RETURNING возвращает указанное поле
# car_id = 6
# with conn.cursor() as curs:
#     curs.execute(
#         "INSERT INTO cars (brand, model) VALUES (%s, %s)\
#             RETURNING id AS current_id;",
#         (brand, model)
#     )
#     res = curs.fetchone()[0]
#     print(res)
#     conn.commit()
#     curs.execute("DELETE FROM cars WHERE id=%s;", (res,))
#     print(curs.fetchall())
#     conn.commit()
# conn.close()

# # работает ))
# with conn.cursor() as curs:
#     cars = [("Bob", "bob@mail.com"), ("Alice", "alice@mail.com"),
#             ("John", "john@mail.com")]
#     execute_values(curs, "INSERT INTO cars (brand, model) VALUES %s", cars)
#     conn.commit()
#     print(curs.rowcount)    # кол-во изменений в базе
# conn.close()
