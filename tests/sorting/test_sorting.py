import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "min_salary": "5000",
            "max_salary": "6279",
            "date_posted": "2020-06-07"
        },
        {
            "min_salary": "2000",
            "max_salary": "3279",
            "date_posted": "2020-01-07"
        },
        {
            "min_salary": "7000",
            "max_salary": "8279",
            "date_posted": "2020-03-07"
        },
    ]

    min_salary_order = [
        {
            "min_salary": "2000",
            "max_salary": "3279",
            "date_posted": "2020-01-07"
        },
        {
            "min_salary": "5000",
            "max_salary": "6279",
            "date_posted": "2020-06-07"
        },
        {
            "min_salary": "7000",
            "max_salary": "8279",
            "date_posted": "2020-03-07"
        },
    ]

    max_salary_order = [
        {
            "min_salary": "7000",
            "max_salary": "8279",
            "date_posted": "2020-03-07"
        },
        {
            "min_salary": "5000",
            "max_salary": "6279",
            "date_posted": "2020-06-07"
        },
        {
            "min_salary": "2000",
            "max_salary": "3279",
            "date_posted": "2020-01-07"
        }
    ]

    date_posted_order = [
        {
            "min_salary": "5000",
            "max_salary": "6279",
            "date_posted": "2020-06-07"
        },
        {
            "min_salary": "7000",
            "max_salary": "8279",
            "date_posted": "2020-03-07"
        },
        {
            "min_salary": "2000",
            "max_salary": "3279",
            "date_posted": "2020-01-07"
        }
    ]

    sort_by(jobs, "min_salary")
    assert jobs == min_salary_order

    sort_by(jobs, "max_salary")
    assert jobs == max_salary_order

    sort_by(jobs, "date_posted")
    assert jobs == date_posted_order

    with pytest.raises(ValueError):
        sort_by(jobs, "title")
