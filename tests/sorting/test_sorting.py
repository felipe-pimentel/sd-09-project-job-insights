from src.sorting import max_salary_key, sort_by
import pytest


@pytest.fixture
def jobs():
    return []


@pytest.fixture
def criteria():
    return {
        "date_posted": "date_posted_key",
        "max_salary": "max_salary_key",
        "min_salary": "min_salary_key",
    }


def test_sort_by_criteria(jobs, criteria):
    invalid_criteria = "xablau"
    with pytest.raises(
        ValueError, match="invalid sorting criteria: " + invalid_criteria
    ):
        sort_by(jobs, invalid_criteria)
