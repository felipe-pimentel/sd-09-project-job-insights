import pytest
from src.sorting import sort_by

payload_job_1 = {
    "max_salary": 100,
    "min_salary": 1000,
    "data_posted": "2000-01-01",
}
payload_job_2 = {"max_salary": "", "min_salary": "", "data_posted": ""}
payload_job_3 = {
    "max_salary": 10000,
    "min_salary": 10,
    "data_posted": "2010-10-01",
}
jobs = [payload_job_1, payload_job_2, payload_job_3]

min_salary_expected_result = [payload_job_3, payload_job_1, payload_job_2]
max_salary_expected_result = [payload_job_3, payload_job_1, payload_job_2]
data_posted_expected_result = [payload_job_3, payload_job_1, payload_job_2]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == min_salary_expected_result

    sort_by(jobs, "max_salary")
    assert jobs == max_salary_expected_result

    sort_by(jobs, "data_posted")
    assert jobs == data_posted_expected_result

    with pytest.raises(ValueError):
        sort_by(jobs, "invalid_criteria")
