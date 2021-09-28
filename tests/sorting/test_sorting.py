from src.sorting import sort_by


def test_sort_by_criteria():
    JOBS = [
        {
            "min_salary": "1000",
            "max_salary": "8000",
            "date_posted": "2020-08-28",
        },
        {
            "min_salary": "2000",
            "max_salary": "7000",
            "date_posted": "2021-08-28",
        },
        {
            "min_salary": "7777",
            "max_salary": "14444",
            "date_posted": "2020-12-25",
        },
    ]
    sort_by(JOBS, "max_salary")
    assert JOBS[0]["max_salary"] == "14444"

    sort_by(JOBS, "min_salary")
    assert JOBS[0]["min_salary"] == "1000"

    sort_by(JOBS, "date_posted")
    assert JOBS[0]["date_posted"] == "2021-08-28"
