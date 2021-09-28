import pytest
from src.sorting import sort_by

jobs_mock = [
    {"min_salary": 1, "max_salary": 7, "date_posted": "2021-09-28"},
    {"min_salary": 5, "max_salary": 9, "date_posted": "2021-09-29"},
]


def test_sort_by_criteria():

    sort_by(jobs_mock, "min_salary")
    assert jobs_mock == [
        {"min_salary": 1, "max_salary": 7, "date_posted": "2021-09-28"},
        {"min_salary": 5, "max_salary": 9, "date_posted": "2021-09-29"},
    ]

    sort_by(jobs_mock, "max_salary")
    assert jobs_mock == [
        {"min_salary": 5, "max_salary": 9, "date_posted": "2021-09-29"},
        {"min_salary": 1, "max_salary": 7, "date_posted": "2021-09-28"},
    ]

    sort_by(jobs_mock, "date_posted")
    assert jobs_mock == [
        {"min_salary": 5, "max_salary": 9, "date_posted": "2021-09-29"},
        {"min_salary": 1, "max_salary": 7, "date_posted": "2021-09-28"},
    ]

    with pytest.raises(ValueError):
        sort_by(jobs_mock, "invalid_criteria")
    # pass
