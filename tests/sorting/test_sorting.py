from src.sorting import sort_by


def test_sort_by_criteria():
    JOBS = [
        {
            "min_salary": "100",
            "max_salary": "1000",
            "date_posted": "2020-10-01",
        },
        {
            "min_salary": "1000",
            "max_salary": "10000",
            "date_posted": "2021-10-01",
        },
        {
            "min_salary": "200",
            "max_salary": "20000",
            "date_posted": "2021-10-02",
        },
    ]
    sort_by(JOBS, "max_salary")
    assert JOBS[0]["max_salary"] == "20000"

    sort_by(JOBS, "min_salary")
    assert JOBS[0]["min_salary"] == "100"

    sort_by(JOBS, "date_posted")
    assert JOBS[0]["date_posted"] == "2021-10-02"
