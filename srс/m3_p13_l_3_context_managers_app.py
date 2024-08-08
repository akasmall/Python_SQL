import psycopg2

conn = psycopg2.connect('postgresql://tirion:secret@localhost:5432/tirion')


# BEGIN (write your solution here)
def make_cars_table(conn_):
    sql = "CREATE TABLE cars (\
        id SERIAL PRIMARY KEY, brand VARCHAR(100), model VARCHAR(100))"
    # sql_db_is = "SELECT EXISTS (SELECT 1 FROM information_schema.tables\
    #     WHERE table_name = 'cars')"
    # with conn_:
    with conn_.cursor() as curs:
        curs.execute("DROP TABLE IF EXISTS cars;")
        conn.commit()
        curs.execute(sql)
        conn.commit()
        # curs.close()


def populate_cars_table(conn_, cars_):
    sql = "INSERT INTO cars (brand, model) VALUES %s, %s;"
    with conn_:
        with conn_.cursor() as curs:
            curs.execute(sql, cars_)
            conn.commit()
        # curs.close()


def get_all_cars(conn_):
    sql = "SELECT brand, model FROM cars ORDER BY brand;"
    with conn_:
        with conn_.cursor() as curs:
            curs.execute(sql)
            result = list(curs)
            conn.commit()
    return result

# END


make_cars_table(conn)
# get_all_cars(conn)  # []


cars = [('kia', 'sorento'), ('bmw', 'x5')]
populate_cars_table(conn, cars)
res = get_all_cars(conn)
print(res)
# # [(1, 'kia', 'sorento'),
# #  (2, 'bmw', 'x5')]

# !src / solution.py
# *Напишите функцию make_cars_table(), которая принимает соединение и
# создает в базе данных таблицу cars.

# *Таблица должна содержать следующие поля:

# *id — идентификатор автомобиля, первичный ключ, который автоматически
# генерируется базой данных
# *brand — марка автомобиля
# *model — модель автомобиля

# *Напишите функцию populate_cars_table(), которая принимает соединение и список
# автомобилей, и добавляет их в таблицу cars

# *Наконец, напишите функцию get_all_cars(), которая принимает соединение,
# и возвращает все автомобили, которые содержатся в базе данных в таблице cars.
# *Записи должны быть отсортированы по марке автомобиля в прямом порядке.
# *Для автоматического закрытия соединения используйте контекстный менеджер.

# conn = psycopg2.connect('..')

# make_cars_table(conn)
# get_all_cars(conn)  # []


# cars = [('kia', 'sorento'), ('bmw', 'x5')]
# populate_cars_table(conn, cars)
# get_all_cars(conn)
# # [(1, 'kia', 'sorento'),
# #  (2, 'bmw', 'x5')]
# ?Подсказки
# ?Для первичного ключа используйте тип данных SERIAL
