from src.sorting import sort_by

JOB_A = {
    "max_salary": 2000,
    "min_salary": 500,
    "date_posted": "2014-07-08",
}

JOB_B = {
    "max_salary": 6000,
    "min_salary": 200,
    "date_posted": "2007-08-06",
}

JOB_C = {
    "max_salary": 1000,
    "min_salary": 100,
    "date_posted": "2008-08-14",
}


def test_sort_by_criteria():
    jobs_mock = [JOB_A, JOB_B, JOB_C]

    sort_by(jobs_mock, "min_salary")
    assert jobs_mock == [JOB_C, JOB_B, JOB_A]

    sort_by(jobs_mock, "max_salary")
    assert jobs_mock == [JOB_B, JOB_A, JOB_C]

    sort_by(jobs_mock, "date_posted")
    assert jobs_mock == [JOB_A, JOB_C, JOB_B]
