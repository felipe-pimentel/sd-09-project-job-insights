import pytest
from src.sorting import sort_by


@pytest.fixture
def jobs():
    """Nosso cenário (contexto) temos os seguintes salários e data"""
    return [
        {
            "min_salary": 2000,
            "max_salary": 3000,
            "date_posted": "2021-10-04",
        },
        {
            "min_salary": 1000,
            "max_salary": 2000,
            "date_posted": "2021-10-05",
        },
        {
            "min_salary": 500,
            "max_salary": 1500,
            "date_posted": "2021-10-06",
        },
        {
            "min_salary": 800,
            "max_salary": 1800,
            "date_posted": "2021-10-07",
        },
    ]


def test_sort_by_criteria(jobs):
    sort_by(jobs, "min_salary")
    min_salary = []
    for job in jobs:
        min_salary.append(job["min_salary"])
    assert min_salary == [500, 800, 1000, 2000]

    sort_by(jobs, "max_salary")
    max_salary = []
    for job in jobs:
        max_salary.append(job["max_salary"])
    assert max_salary == [3000, 2000, 1800, 1500]

    sort_by(jobs, "date_posted")
    date_posted = []
    for job in jobs:
        date_posted.append(job["date_posted"])
    assert date_posted == [
        "2021-08-22",
        "2021-08-21",
        "2021-08-20",
        "2021-08-19",
    ]
