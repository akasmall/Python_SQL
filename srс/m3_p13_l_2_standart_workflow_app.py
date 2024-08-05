import psycopg2

conn = psycopg2.connect('postgresql://tirion:secret@localhost:5432/tirion')


# BEGIN (write your solution here)
def get_all_movies(conn_):
    sql1 = "SELECT title, release_year, duration FROM movies;"
    cursor = conn_.cursor()
    cursor.execute(sql1)
    result = cursor.fetchall()
    cursor.close()
    return result


def add_movies(conn_):
    sql2 = "INSERT INTO movies(title, release_year, duration) \
        VALUES('Godfather', 175, 1972)"
    cursor = conn_.cursor()
    cursor.execute(sql2)
    cursor.close()

    sql3 = "INSERT INTO movies(title, release_year, duration) \
        VALUES('The Green Mile', 189, 1999)"
    cursor = conn_.cursor()
    cursor.execute(sql3)
    # cursor.close()

    conn_.commit()  # Коммитим, т.е. сохраняем изменения в БД
    # conn_.close()  # Соединение нужно закрыть
    return


def del_movies(conn_):
    sql3 = "DELETE FROM movies WHERE id > 3"
    cursor = conn_.cursor()
    cursor.execute(sql3)
    cursor.close()
    conn_.commit()  # Коммитим, т.е. сохраняем изменения в БД

# END


# del_movies(conn)

# add_movies(conn)
# print(res)

res = get_all_movies(conn)
conn.close()
print(res)
print()
# # [(1, 'The Dark Knight', 2008, 152),
# # (2, '12 Angry Men', 1957, 96),
# # (3, 'Pulp Fiction', 1994, 154)]


# !В этом упражнении уже создано соединение с базой данных и таблица movies,
# !которая содержит информацию о фильмах.
# *Таблица содержит следующие поля:

# *id — идентификатор фильма, первичный ключ, генерируется базой данных
# автоматически
# *title — название фильма
# *release_year — год выпуска на экран
# *duration — длительность фильма в минутах

# !src / solution.py
# *Напишите функцию add_movies(). Функция принимает соединение с БД и должна
# *добавить в таблицу movies два фильма:

# 'Godfather' длительностью 175 минут, выпущенный в 1972 году
# 'The Green Mile' длительностью 189 минут, выпущенный в 1999 году

# *Напишите также функцию get_all_movies(). Функция принимает соединение
# *с БД и должна получить список всех фильмов, которые содержатся в базе
# *данных в таблице movies. Каждый фильм — это новая строка
# *формата Godfather 1972 175.

# conn = psycopg2.connect('..')

# get_all_movies(conn)
# # [(1, 'The Dark Knight', 2008, 152),
# # (2, '12 Angry Men', 1957, 96),
# # (3, 'Pulp Fiction', 1994, 154)]

# add_movies(conn)

# get_all_movies(conn)
# # [(1, 'The Dark Knight', 2008, 152),
# # (2, '12 Angry Men', 1957, 96),
# # (3, 'Pulp Fiction', 1994, 154),
# # (4, 'Godfather', 1972, 175),
# # (5, 'The Green Mile', 1999, 189)]

# решение ментора
# !# BEGIN
# !def add_movies(conn):
#     curs = conn.cursor()
#     sql = "INSERT INTO movies (title, release_year, duration) VALUES %s, %s;"
#   curs.execute(sql, (('Godfather', 1972, 175), ('The Green Mile', 1999, 189)))
#     conn.commit()


# !def get_all_movies(conn):
#     curs = conn.cursor()
#     sql = "SELECT * FROM movies;"
#     curs.execute(sql)
#     conn.commit()
#     return list(curs)
# !# END
