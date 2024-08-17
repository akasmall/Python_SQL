# BEGIN (write your solution here)
from dataclasses import dataclass
from typing import Optional
import decimal


@dataclass
class Product:
    """Класс, представляющий товар в магазине"""
    id: Optional[int] = None
    name: str
    description: str
    price: decimal


def get_product(name_):
    return name_

# END


# !Представьте, что существует маленький магазинчик фруктов, в котором
# работает всего один продавец. Он не помнит все цены на товары и когда
# приходит покупатель, начинает искать цену в своем журнале. Это занимает
# довольно много времени, покупатели нервничают. Гораздо проще было бы,
# если бы у него был электронный каталог, куда бы он мог ввести название
# товара и получить всю информацию о нем из базы данных. В этом упражнении
# вам предстоит разработать такое приложение

# ?src / product.py
# *Создайте класс Product, который будет представлять собой товар в нашем
# магазине. У товара есть уникальный идентификатор, название, описание и цена.
# Добавьте в класс необходимые свойства и методы по своему усмотрению

# ?scr / productDAO.py
# *Создайте класс ProductDAO, который предназначен для работы с таблицей
# *товаров products. Создайте в классе метод, который будет получать
# *из таблицы данные о товаре по его названию и возвращать объект товара.
# *Считаем, что название товара в таблице уникально. Таблица имеет
# *следующую структуру:

# *products

# *id - id товара
# *name - название товара
# *description - описание
# *price - цена

# ?scr / catalog.py
# *Сам каталог. В классе Catalog создайте метод get_product(), который
# *возвращает информацию о товаре. Метод принимает один параметр — название
# *товара, строку. Метод должен вернуть словарь — полную информацию о товаре,
# *который содержит его идентификатор, название, цену и описание.

# conn = ...  # Создаем соединение
# catalog = Catalog(conn)

# info = catalog.get_product('apple')
# # {
# #  'id': 2,
# #  'name': 'apple',
# #  'description': 'red fruit',
# #  'price': 60
# # }
# Если такого товара в базе данных нет, метод должен выбросить
# исключение KeyError с сообщением, что товар не найден.

# Пример сообщения

# KeyError: Product dragonfruit not found

# DROP TABLE IF EXISTS products

# CREATE TABLE products(
#     id serial PRIMARY KEY,
#     name varchar(255),
#     description varchar(255),
#     price integer
# )

# INSERT INTO products(name, description, price) VALUES
# ('banana', 'yellow fruit', 50),
# ('apple', 'red fruit', 60),
# ('orange', 'orange citrus fruit', 40),
# ('strawberry', 'small red fruit', 70),
# ('pineapple', 'tropical fruit with spiky skin', 80),
# ('watermelon', 'large green striped fruit', 30),
# ('kiwi', 'small brown fuzzy fruit', 65),
# ('grape', 'small round fruit growing in bunches', 55),
# ('cherry', 'small round red fruit with pit', 75),
# ('pear', 'pear-shaped fruit with sweet white flesh', 45)
