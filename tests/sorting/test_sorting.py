from src.sorting import sort_by
import pytest


def test_sort_by_criteria():
    first_job = {
        "job_title": "Engineer",
        "min_salary": 3000,
        "max_salary": 8000,
        "date_posted": "2020-05-08",
    }

    second_job = {
        "job_title": "Doctor",
        "min_salary": 3800,
        "max_salary": 7000,
        "date_posted": "2020-04-25",
    }

    third_job = {
        "job_title": "Lawyer",
        "min_salary": 3500,
        "max_salary": 5500,
        "date_posted": "2020-05-02",
    }

    jobs_list = [first_job, second_job, third_job]
    min_salary_list = [third_job, second_job, first_job]
    max_salary_list = [first_job, second_job, third_job]
    date_posted_list = [first_job, third_job, second_job]

    sort_by(jobs_list, "min_salary")
    assert jobs_list == min_salary_list

    sort_by(jobs_list, "max_salary")
    assert jobs_list == max_salary_list

    sort_by(jobs_list, "date_posted")
    assert jobs_list == date_posted_list

    with pytest.raises(
        ValueError, match="invalid sorting criteria: other_criteria"
    ):
        sort_by(jobs_list, "other_criteria")
