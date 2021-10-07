from src.sorting import sort_by

jobs_mock = [
    {
        "date_posted": "2021-03-03",
        "max_salary": 30000,
        "min_salary": 3000
    },
    {
        "date_posted": "2021-01-01",
        "max_salary": 10000,
        "min_salary": 1000
    },
    {
        "date_posted": "2021-02-02",
        "max_salary": 20000,
        "min_salary": 2000
    }
]


def test_sort_by_criteria():
    sort_by(jobs_mock, "min_salary")
    assert jobs_mock[0]["min_salary"] == 1000
    assert jobs_mock[1]["min_salary"] == 2000
    assert jobs_mock[2]["min_salary"] == 3000

    sort_by(jobs_mock, "max_salary")
    assert jobs_mock[0]["max_salary"] == 30000
    assert jobs_mock[1]["max_salary"] == 20000
    assert jobs_mock[2]["max_salary"] == 10000

    sort_by(jobs_mock, "date_posted")
    assert jobs_mock[0]["date_posted"] == "2021-03-03"
    assert jobs_mock[1]["date_posted"] == "2021-02-02"
    assert jobs_mock[2]["date_posted"] == "2021-01-01"
