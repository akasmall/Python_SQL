import psycopg2
# from psycopg2.extras import DictCursor

conn = psycopg2.connect('postgresql://tirion:secret@localhost:5432/tirion')


# BEGIN (write your solution here)
def create_post(conn_, post_dst):
    sql = """INSERT INTO posts \
            (title, content, author_id)\
            VALUES (%s, %s, %s) RETURNING id"""
    with conn_.cursor() as curs:
        curs.execute(
            sql,
            (post_dst['title'], post_dst['content'], post_dst['author_id'])
        )
        new_post_id = curs.fetchone()[0]
        conn_.commit()
    return new_post_id


def add_comment(conn_, comm_dst):
    sql = """INSERT INTO comments \
        (post_id, author_id, content)\
        VALUES (%s, %s, %s) RETURNING id"""
    with conn_.cursor() as curs:
        curs.execute(
            sql,
            (comm_dst['post_id'], comm_dst['author_id'], comm_dst['content'])
        )
        new_comm_id = curs.fetchone()[0]
        conn_.commit()
    return new_comm_id


def get_latest_posts(conn_, qnt):
    sql_posts = "SELECT * FROM posts ORDER BY created_at desc LIMIT %s"
    sql_comm = "SELECT * FROM comments WHERE post_id = %s"
    with conn_.cursor() as curs:
        curs.execute(sql_posts, (qnt, ))
        columns = [desc[0] for desc in curs.description]
        res_post = [dict(zip(columns, row)) for row in curs.fetchall()]
        conn_.commit()
    if not res_post:
        return []
    with conn_.cursor() as curs:
        curs.execute(sql_comm, (res_post[0]['id'], ))
        # results = curs.fetchall()
        columns = [desc[0] for desc in curs.description]
        res_comm = [dict(zip(columns, row)) for row in curs.fetchall()]
        conn_.commit()

    res_post[0]['comments'] = res_comm
    return res_post

# END


print(get_latest_posts(conn, 1))

# post = {'title': 'My Super Post', 'content': 'text', 'author_id': 42}
# res_01 = create_post(conn, post)  # 1

# comment = {'post_id': 1, 'author_id': 42, 'content': 'wow such post'}
# res_02 = add_comment(conn, comment)  # 1


print()

# !В этом упражнении уже создано соединение с базой данных и следующие таблицы:

# *posts, которая содержит информацию о постах:

# *id — id поста, первичный ключ, генерируется базой данных автоматически
# *title — название поста
# *content — содержание поста
# *author_id — id автора
# *created_at - дата создания поста, генерируется автоматически
# *comments, которая содержит информацию о комментариях:

# *id - id комментария, первичный ключ, генерируется базой данных автоматически
# *post_id - id поста, к которому оставлен комментарий
# *author_id - id автора
# *content - содержание комментария
# *created_at - дата создания комментария, генерируется автоматически

# !src / solution.py
# ?Реализуйте следующие функции:

# ?create_post() - принимает соединение с базой данных и словарь с данными
# поста. Словарь должен содержать ключи: 'title', 'content', 'author_id'.
# Функция должна создать новый пост и вернуть его id.

# ?add_comment() - принимает соединение с базой данных и словарь с данными
# комментария. Словарь должен содержать ключи: 'post_id', 'author_id',
# 'content'. Функция должна добавить новый комментарий и вернуть его id.

# ?get_latest_posts() - принимает соединение с базой данных и количество
# постов. Возвращает список n последних постов с их комментариями.
# Каждый элемент списка должен быть словарем с ключами: 'id', 'title',
# 'content', 'author_id', 'created_at', 'comments'. 'comments' - это список
# словарей с ключами: 'id', 'author_id', 'content', 'created_at'

# conn = psycopg2.connect('..')

# get_latest_posts(conn, 1)
# # []

# post = {'title': 'My Super Post', 'content': 'text', 'author_id': 42}
# create_post(conn, post)  # 1

# comment = {'post_id': 1, 'author_id': 42, 'content': 'wow such post'}
# add_comment(conn, comment)  # 1

# get_latest_posts(conn, 1)
# # [{
# # 'id': 1,
# # 'title': 'My Super Post',
# # 'content': 'text',
# # 'author_id': 42,
# # 'created_at': datetime.datetime(2022, 7, 19, 14, 32, 37, 123857),
# # 'comments': [
# #  {
# #   'id': 1,
# #   'author_id': 42,
# #   'content': 'wow such post',
# #   'created_at': datetime.datetime(2022, 8, 19, 14, 32, 37, 135319)
# #   }
# #  ]}]

# !решение ментора
# ?# BEGIN
# *def create_post(conn, post):
#     with conn.cursor() as cur:
#         cur.execute("""
#             INSERT INTO posts (title, content, author_id)
#             VALUES (%(title)s, %(content)s, %(author_id)s)
#             RETURNING id
#         """, post)
#         post_id = cur.fetchone()[0]
#     conn.commit()
#     return post_id


# *def add_comment(conn, comment):
#     with conn.cursor() as cur:
#         cur.execute("""
#             INSERT INTO comments (post_id, author_id, content)
#             VALUES (%(post_id)s, %(author_id)s, %(content)s)
#             RETURNING id
#         """, comment)
#         comment_id = cur.fetchone()[0]
#     conn.commit()
#     return comment_id


# *def get_latest_posts(conn, n):
#     with conn.cursor(cursor_factory=DictCursor) as cur:
#         cur.execute("""
#             SELECT
#                 p.*,
#                 c.id as comment_id,
#                 c.author_id as comment_author_id,
#                 c.content as comment_content,
#                 c.created_at as comment_created_at
#             FROM posts p
#             LEFT JOIN comments c ON p.id = c.post_id
#             WHERE p.id IN (
#                 SELECT id FROM posts
#                 ORDER BY created_at DESC
#                 LIMIT %s
#             )
#             ORDER BY p.created_at DESC, c.created_at DESC
#         """, (n,))

#         rows = cur.fetchall()

#         posts_dict = {}
#         for row in rows:
#             post_id = row['id']
#             if not posts_dict.get(post_id):
#                 posts_dict[post_id] = {
#                     'id': row['id'],
#                     'title': row['title'],
#                     'content': row['content'],
#                     'author_id': row['author_id'],
#                     'created_at': row['created_at'],
#                     'comments': []
#                 }

#             if row.get('comment_id'):
#                 posts_dict[post_id]['comments'].append({
#                     'id': row['comment_id'],
#                     'author_id': row['comment_author_id'],
#                     'content': row['comment_content'],
#                     'created_at': row['comment_created_at']
#                 })

#         return list(posts_dict.values())
# ?# END
