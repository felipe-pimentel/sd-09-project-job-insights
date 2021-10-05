from src.sorting import sort_by
import pytest


def test_sort_by_criteria():
    jobs = [
        {"min_salary": 10, "max_salary": 30, "date_posted": "05-12-2019"},
        {"min_salary": 60, "max_salary": 90, "date_posted": "04-13-2019"},
        {"min_salary": 20, "max_salary": 50, "date_posted": "12-01-2019"},
    ]

    ordered_by_max_salary = [
        {"min_salary": 60, "max_salary": 90, "date_posted": "04-13-2019"},
        {"min_salary": 20, "max_salary": 50, "date_posted": "12-01-2019"},
        {"min_salary": 10, "max_salary": 30, "date_posted": "05-12-2019"},
    ]

    ordered_by_min_salary = [
        {"min_salary": 10, "max_salary": 30, "date_posted": "05-12-2019"},
        {"min_salary": 20, "max_salary": 50, "date_posted": "12-01-2019"},
        {"min_salary": 60, "max_salary": 90, "date_posted": "04-13-2019"},
    ]

    sort_by(jobs, "max_salary")

    assert jobs == ordered_by_max_salary

    sort_by(jobs, "min_salary")

    assert jobs == ordered_by_min_salary

    with pytest.raises(
        ValueError, match="invalid sorting criteria: date-posted"
    ):
        sort_by(jobs, "date-posted")
