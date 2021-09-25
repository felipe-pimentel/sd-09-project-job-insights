import pytest
from src.sorting import sort_by


#  Às precondições ou estados necessários para a execução de um teste,
# damos o nome de test fixture ou apenas fixture .
@pytest.fixture
def jobs():
    return [
        {"min_salary": 250, "max_salary": 750, "data_posted": "2021-01-08"},
        {"min_salary": 650, "max_salary": 2350, "data_posted": "2021-05-22"},
        {"min_salary": 1300, "max_salary": 5000, "data_posted": "2021-09-24"},
    ]


def test_sort_by_criteria(jobs):
    sort_by(jobs, "min_salary")
    #  assert varre o arquivo
    assert [job["min_salary"] for job in jobs] == [250, 650, 1300]

    sort_by(jobs, "max_salary")
    assert [job["max_salary"] for job in jobs] == [5000, 2350, 750]

    sort_by(jobs, "date_posted")
    assert [job["date_posted"] for job in jobs] == [
        "2021-09-24",
        "2021-05-22",
        "2021-01-08",
    ]
