from src.sorting import sort_by

jobs_mock = [
    {
        "job_title": "test job 1",
        "min_salary": 1000,
        "max_salary": 3000,
        "date_posted": "2020-02-02"
    },
    {
        "job_title": "test job 2",
        "min_salary": 4000,
        "max_salary": 7000,
        "date_posted": "2021-02-02"
    },
    {
        "job_title": "test job 3",
        "min_salary": 5000,
        "max_salary": 7500,
        "date_posted": "2021-10-02"
    },
    {
        "job_title": "test job 4",
        "min_salary": 2000,
        "max_salary": 3500,
        "date_posted": "2021-10-10"
    },
    {
        "job_title": "test job 5",
        "min_salary": 8000,
        "max_salary": 9500,
        "date_posted": "2020-10-10"
    },
]

criteria = ["date_posted", "max_salary", "min_salary"]


def test_sort_by_criteria():
    # testing by date posted
    sort_by(jobs_mock, criteria[0])
    assert jobs_mock[0]["date_posted"] == "2021-10-10"
    assert jobs_mock[1]["date_posted"] == "2021-10-02"
    assert jobs_mock[2]["date_posted"] == "2021-02-02"
    assert jobs_mock[3]["date_posted"] == "2020-10-10"
    assert jobs_mock[4]["date_posted"] == "2020-02-02"

    # testing by max salary
    sort_by(jobs_mock, criteria[0])
    assert jobs_mock[0]["max_salary"] == 9500
    assert jobs_mock[1]["max_salary"] == 7500
    assert jobs_mock[2]["max_salary"] == 7000
    assert jobs_mock[3]["max_salary"] == 3500
    assert jobs_mock[4]["max_salary"] == 3000

    # testing by min salary
    sort_by(jobs_mock, criteria[0])
    assert jobs_mock[0]["min_salary"] == 1000
    assert jobs_mock[1]["min_salary"] == 2000
    assert jobs_mock[2]["min_salary"] == 4000
    assert jobs_mock[3]["min_salary"] == 5000
    assert jobs_mock[4]["min_salary"] == 8000
