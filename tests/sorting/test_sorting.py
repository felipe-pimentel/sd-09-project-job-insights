from src.sorting import sort_by
import pytest

'#informação fixa que será usada mais de uma vez, apenas retorna uma lista'


@pytest.fixture
def order_criteria():
    return [
        {'min_salary': 800, 'max_salary': 5000, 'date_posted': '2021-10-23'},
        {'min_salary': 1000, 'max_salary': 7000, 'date_posted': '2021-09-23'},
        {'min_salary': 1200, 'max_salary': 9000, 'date_posted': '2021-08-23'},
    ]


def test_sort_by_criteria(order_criteria):
    '# prepara o terreno'
    sort_by(order_criteria, 'min_salary')
    min_salary = []
    '#executa'
    for low in order_criteria:
        min_salary.append(low['min_salary'])
    '#confere os dados'
    assert min_salary == [800, 1000, 1200]

    sort_by(order_criteria, 'max_salary')
    max_salary = []
    for high in order_criteria:
        max_salary.append(high['max_salary'])
    assert max_salary == [9000, 7000, 5000]
