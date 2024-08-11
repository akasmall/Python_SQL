import sys
# from dataclasses import dataclass   # из файла models.py
# from typing import Optional   # из файла models.py
import psycopg2
from psycopg2.extras import NamedTupleCursor
from srс.m3_p13_l_7__dao_models import Course, Lesson


# @dataclass
# class Course:
#     name: str
#     description: str
#     id: Optional[int] = None


# @dataclass
# class Lesson:
#     name: str
#     text: str
#     course_id: int
#     id: Optional[int] = None


conn = psycopg2.connect('postgresql://tirion:secret@localhost:5432/tirion')


def commit(conn_):
    conn_.commit()


def save_course(conn_, course_):
    with conn_.cursor(cursor_factory=NamedTupleCursor) as cur:
        if course_.id is None:
            cur.execute(
                """INSERT INTO courses (name, description)
                VALUES (%s, %s) RETURNING id;""",
                (course_.name, course_.description)
            )
            course_.id = cur.fetchone().id
        else:
            cur.execute(
                "UPDATE courses SET name = %s, description = %s WHERE id = %s;",
                (course_.name, course_.description, course_.id)
            )
    return course_.id


def find_course(conn_, course_id_):
    with conn_.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute("SELECT * FROM courses WHERE id = %s;", (course_id_,))
        result = cur.fetchone()
        if result:
            return Course(
                id=result.id,
                name=result.name,
                description=result.description
            )
    return None


def get_all_courses(conn_):
    courses = []
    with conn_.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute("SELECT * FROM courses;")
        for row in cur.fetchall():
            courses.append(Course(
                id=row.id,
                name=row.name,
                description=row.description
            ))
        return courses


# BEGIN (write your solution here)
def save_lesson(conn_, lesson_):
    with conn_.cursor(cursor_factory=NamedTupleCursor) as cur:
        if lesson_.id is None:
            cur.execute(
                """INSERT INTO lessons (name, text, course_id)
                VALUES (%s, %s, %s) RETURNING id;""",
                (lesson_.name, lesson_.text, lesson_.course_id)
            )
            lesson_.id = cur.fetchone().id
        else:
            cur.execute(
                """UPDATE lessons SET name = %s, text = %s, course_id = %s
                WHERE id = %s;""",
                (lesson_.name, lesson_.text, lesson_.id, lesson_.course_id)
            )
    return lesson_.id


def find_lesson(conn_, course_id_):
    with conn_.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute("SELECT * FROM lessons WHERE id = %s;", (course_id_,))
        result = cur.fetchone()
        if result:
            return Lesson(
                id=result.id,
                name=result.name,
                text=result.text,
                course_id=result.course_id
            )
    return None


def get_course_lessons(conn_, course_id_):
    courses = []
    with conn_.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(
            "SELECT * FROM lessons WHERE course_id = %s;", (course_id_,)
        )
        for row in cur.fetchall():
            courses.append(Lesson(
                id=row.id,
                name=row.name,
                text=row.text,
                course_id=row.course_id
            ))
        return courses

# END


course = Course('test_course', 'test_description')
course_id = save_course(conn, course)
commit(conn)
found_course = find_course(conn, course_id)
commit(conn)
if found_course.name != course.name:
    print('Нет курса')
    sys.exit(0)

lesson1 = Lesson('test_lesson_1', 'test_text_1', course_id)
lesson2 = Lesson('test_lesson_2', 'test_text_2', course_id)

lesson1_id = save_lesson(conn, lesson1)
commit(conn)
lesson2_id = save_lesson(conn, lesson2)
commit(conn)
found_lesson_2 = find_lesson(conn, lesson2_id)
if found_lesson_2.name != lesson2.name:
    print('Нет уроков')
    sys.exit(0)
all_lessons = get_course_lessons(conn, course_id)
if [lesson1, lesson2] == all_lessons:
    print("все гуд")


# !описание баз в упражнении
# *DROP TABLE IF EXISTS courses
# *DROP TABLE IF EXISTS lessons

# *CREATE TABLE courses(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     description TEXT NOT NULL
# )

# *CREATE TABLE lessons(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     text TEXT NOT NULL,
#     course_id INTEGER NOT NULL,
#     FOREIGN KEY(course_id) REFERENCES courses(id)
# )

# !src / solution.py
# Мы уже рассмотрели методы сохранения и поиска конкретной сущности в таблице.
# В дополнение к ним, может понадобиться метод для извлечения всех сущностей
# из таблицы. В этом упражнении вам предстоит создать такой метод.

# ?src / models.py
# *В упражнении уже созданы модели для сущностей Course и Lesson

# ?src / solution.py
# *В упражнении уже созданы функции для работы с таблицей курсов courses.
# *Есть функции для сохранения курса и поиска конкретного курса по его
# *идентификатору.

# ?Создайте функции для работы с сущностью Lesson:

# *save_lesson() - принимает соединение и урок, сохраняет его в базу
# и возвращает id урока
# *find_lesson() - принимает соединение и id урока, и возращает его из базы
# *get_course_lessons() - принимает соединение и id курса, и возвращает
# все уроки, связанные с этим курсом

# решение ментора
