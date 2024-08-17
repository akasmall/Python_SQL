from dataclasses import dataclass
import decimal
from typing import Optional
import psycopg2
from psycopg2.extras import DictCursor
# from srс.product import Product

# BEGIN (write your solution here)


@dataclass
class ProductDAO:
    name: str
    description: str
    price: decimal
    id: Optional[int] = None


def get_product(conn_, name_):
    sql = """
    SELECT name, description, price
    FROM products
    WHERE name = %s;
    """
    with conn_.cursor(cursor_factory=DictCursor) as curs:
        curs.execute(sql, (name_,))
        result = curs.fetchone()
        conn_.commit()
    return result

# END


conn = psycopg2.connect('postgresql://tirion:secret@localhost:5432/tirion')
info = get_product(conn, 'apple')
print(info)
