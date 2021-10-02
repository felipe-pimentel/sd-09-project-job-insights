from src.sorting import sort_by
import pytest


@pytest.fixture
def db_example():
    return [
        {
            "min_salary": 6000,
            "max_salary": 60000,
            "date_posted": "2021-10-18"
        },
        {
            "min_salary": 5000,
            "max_salary": 150000,
            "date_posted": "2021-11-25"
        },
        {
            "min_salary": 7000,
            "max_salary": 80000,
            "date_posted": "2021-01-30"
        }
    ]


def test_sort_by_criteria(db_example):
    sort_by(db_example, "max_salary")
    assert [x["max_salary"] for x in db_example] == [150000, 80000, 60000]

    sort_by(db_example, "min_salary")
    assert [x["min_salary"] for x in db_example] == [5000, 6000, 7000]

    sort_by(db_example, "date_posted")
    assert [x["date_posted"] for x in db_example] == [
        "2021-11-25",
        "2021-10-18",
        "2021-01-30",
        ]

