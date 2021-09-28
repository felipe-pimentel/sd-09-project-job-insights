from src.sorting import sort_by
import pytest


@pytest.fixture
def jobs():
    return [
        {
            "min_salary": "3000",
            "max_salary": "6000",
            "date_posted": "2021-01-20",
        },
        {
            "min_salary": "1000",
            "max_salary": "4000",
            "date_posted": "2021-01-21",
        },
        {
            "min_salary": "2000",
            "max_salary": "5000",
            "date_posted": "2021-01-22",
        },
    ]


@pytest.fixture
def jobs_by_salary_min():
    return [
        {
            "min_salary": "1000",
            "max_salary": "4000",
            "date_posted": "2021-01-21",
        },
        {
            "min_salary": "2000",
            "max_salary": "5000",
            "date_posted": "2021-01-22",
        },
        {
            "min_salary": "3000",
            "max_salary": "6000",
            "date_posted": "2021-01-20",
        },
    ]


@pytest.fixture
def jobs_by_salary_max():
    return [
        {
            "min_salary": "3000",
            "max_salary": "6000",
            "date_posted": "2021-01-20",
        },
        {
            "min_salary": "2000",
            "max_salary": "5000",
            "date_posted": "2021-01-22",
        },
        {
            "min_salary": "1000",
            "max_salary": "4000",
            "date_posted": "2021-01-21",
        },
    ]


@pytest.fixture
def jobs_by_date_post():
    return [
        {
            "min_salary": "2000",
            "max_salary": "5000",
            "date_posted": "2021-01-22",
        },
        {
            "min_salary": "1000",
            "max_salary": "4000",
            "date_posted": "2021-01-21",
        },
        {
            "min_salary": "3000",
            "max_salary": "6000",
            "date_posted": "2021-01-20",
        },
    ]


@pytest.fixture
def criteria():
    return {
        "date_posted": "date_posted_key",
        "max_salary": "max_salary_key",
        "min_salary": "min_salary_key",
    }


def test_sort_by_criteria(
    jobs, jobs_by_date_post, jobs_by_salary_max, jobs_by_salary_min
):
    sort_by(jobs, "date_posted")
    assert jobs == jobs_by_date_post
    sort_by(jobs, "max_salary")
    assert jobs == jobs_by_salary_max
    sort_by(jobs, "min_salary")
    assert jobs == jobs_by_salary_min

    invalid_criteria = "xablau"
    with pytest.raises(
        ValueError, match=f"invalid sorting criteria: {invalid_criteria}"
    ):
        sort_by(jobs, invalid_criteria)
