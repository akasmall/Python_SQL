from srс.m3_p13_l_3_context_managers_app import make_cars_table
from srс.m3_p13_l_3_context_managers_app import populate_cars_table
from srс.m3_p13_l_3_context_managers_app import get_all_cars


def test_solution(db_transaction):
    make_cars_table(db_transaction)
    cars = get_all_cars(db_transaction)
    # assert cars == [] говорят это проблемный код когда сравнение идет с []
    assert cars  # а вот так правильно

    cars = [('lada', 'zaporozhets'), ('cherry', '9')]
    populate_cars_table(db_transaction, cars)

    assert get_all_cars(db_transaction) == [
        (2, 'cherry', '9'),
        (1, 'lada', 'zaporozhets')
    ]
