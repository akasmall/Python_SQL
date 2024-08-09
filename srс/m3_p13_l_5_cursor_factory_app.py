import psycopg2
from psycopg2.extras import DictCursor


conn = psycopg2.connect('postgresql://tirion:secret@localhost:5432/tirion')


# BEGIN (write your solution here)
def get_order_sum(conn_, month_):
    with conn_.cursor(cursor_factory=DictCursor) as curs:
        # sql = "SELECT cts.customer_name as name, SUM(ods.total_amount)\
        #     FROM customers as cts JOIN orders as ods\
        #         ON cts.customer_id = ods.customer_id\
        #     WHERE EXTRACT(MONTH FROM ods.order_date) = %s\
        #     GROUP BY cts.customer_name;"
        curs.execute(
            "SELECT cts.customer_name as name, SUM(ods.total_amount)\
            FROM customers as cts JOIN orders as ods\
                ON cts.customer_id = ods.customer_id\
            WHERE EXTRACT(MONTH FROM ods.order_date) = %s\
            GROUP BY cts.customer_name;",
            (month_,))
        results = curs.fetchall()
        results_for_list = ""
        for row in results:
            results_for_list += (
                f"Покупатель {row[0]} совершил покупок на сумму {int(row[1])}\n"
            )
        # results_for_list = []
        # for row in results:
        #     results_for_list.append(
        #         f"Покупатель {row[0]} совершил покупок на сумму {int(row[1])}"
        #     )
    return results_for_list
# END


# month = 2
# resu = get_order_sum(conn, month)
# print(resu)

# !В практике вам доступны следующие таблицы

# *orders
# *order_id - id заказа
# *customer_id - id покупателя
# *order_date - дата заказа
# *total_amount - сумма заказа
#
# *customers
# *customer_id - id покупателя
# *customer_name - имя покупателя

# !src / solution.py
# ?Допишите функцию get_order_sum(), которая принимает соединение и месяц,
# ?и возвращает общую сумму заказов каждого покупателя за этот месяц.
# ?Функция должна вернуть результат в виде строки:

# *Покупатель Emily White совершил покупок на сумму 290
# *Покупатель John Smith совершил покупок на сумму 130

# conn = psycopg2.connect('..')

# month = 2
# get_order_sum(conn, month)
# # Покупатель Emily White совершил покупок на сумму 290

# !решение ментора
# # BEGIN
# ?def get_order_sum(conn, month):
# *  template = "Покупатель {customer} совершил покупок на сумму {total}".format
#     with conn.cursor(cursor_factory=DictCursor) as cur:
#         query = """
#             SELECT
#                 c.customer_name,
#                 SUM(o.total_amount) AS total
#             FROM
#                 customers c
#             LEFT JOIN
#                 orders o ON c.customer_id = o.customer_id
#             WHERE
#                 EXTRACT(MONTH FROM o.order_date) = %s
#             GROUP BY
#                 c.customer_name;"""
#         month_formated = '{:02d}'.format(month)
#         cur.execute(query, (month_formated,))
#         result = []
#         for row in cur:
#             customer_name = row['customer_name']
#             total = row['total']
# *            result.append(template(customer=customer_name, total=total))
#     conn.commit()

# *    return '\n'.join(result)
# # END
