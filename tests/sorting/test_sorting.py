import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"min_salary": 1000, "max_salary": 10000, "date_posted": "2020-05-08"},
        {"min_salary": 950, "max_salary": 5000, "date_posted": "2020-10-03"},
        {"min_salary": 900, "max_salary": 4000, "date_posted": "2019-05-08"},
    ]

    sort_by(jobs, "min_salary")
    assert jobs == [
        {"min_salary": 900, "max_salary": 4000, "date_posted": "2019-05-08"},
        {"min_salary": 950, "max_salary": 5000, "date_posted": "2020-10-03"},
        {"min_salary": 1000, "max_salary": 10000, "date_posted": "2020-05-08"},
    ]

    sort_by(jobs, "max_salary")
    assert jobs == [
        {"min_salary": 1000, "max_salary": 10000, "date_posted": "2020-05-08"},
        {"min_salary": 950, "max_salary": 5000, "date_posted": "2020-10-03"},
        {"min_salary": 900, "max_salary": 4000, "date_posted": "2019-05-08"},
    ]

    sort_by(jobs, "date_posted")
    assert jobs == [
        {"min_salary": 950, "max_salary": 5000, "date_posted": "2020-10-03"},
        {"min_salary": 1000, "max_salary": 10000, "date_posted": "2020-05-08"},
        {"min_salary": 900, "max_salary": 4000, "date_posted": "2019-05-08"},
    ]

    with pytest.raises(
        ValueError, match="invalid sorting criteria: other_criteria"
    ):
        sort_by(jobs, "other_criteria")

    pass
