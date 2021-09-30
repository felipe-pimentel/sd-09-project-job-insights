from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "max_salary": "1000",
            "min_salary": "10",
            "date_posted": "2020-05-08"
        },
        {
            "max_salary": "1000",
            "min_salary": "100",
            "date_posted": "2020-05-08"
        },
        {
            "max_salary": "10000",
            "min_salary": "200",
            "date_posted": "2020-06-07"
        },
        {
            "max_salary": "15000",
            "min_salary": "0",
            "date_posted": "2020-04-28"
        },
        {
            "max_salary": "1500",
            "min_salary": "5",
            "date_posted": "2020-02-28"
        },
        {
            "max_salary": "1200",
            "min_salary": "10",
            "date_posted": "2020-04-20"
        },
    ]

    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == "15000"

    sort_by(jobs, "min_salary")
    assert jobs[0]["min_salary"] == "0"

    sort_by(jobs, "date_posted")
    assert jobs[0]["date_posted"] == "2020-06-07"
