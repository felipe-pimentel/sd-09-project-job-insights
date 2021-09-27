import pytest
from src.sorting import sort_by


def test_sorting_by_criteria():
    jobs = [
        {"max_salary": 0, "min_salary": 10, "date_posted": "2020-05-08"},
        {"max_salary": 10, "min_salary": 100, "date_posted": "2020-05-08"},
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-06-07"},
        {"max_salary": 15000, "min_salary": 0, "date_posted": "2020-04-28"},
        {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-02-28"},
        {"max_salary": -1, "min_salary": 10, "date_posted": "2020-04-20"},
    ]
    with pytest.raises(ValueError, match="invalid sorting criteria: random"):
        sort_by(jobs, "random")
