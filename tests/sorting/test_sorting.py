from src.sorting import sort_by


def test_sort_by_criteria():
    listJobs = [
        {
            "job_title": "Dev_py",
            "min_salary": 2000,
            "max_salary": 6000,
            "date_posted": "2000-06-18"
        },
        {
            "job_title": "Dev_Java",
            "min_salary": 1000,
            "max_salary": 3500,
            "date_posted": "2020-10-21"
        },
        {
            "job_title": "Dev_C",
            "min_salary": 600,
            "max_salary": 7000,
            "date_posted": "2008-09-15"
        },
        {
            "job_title": "Dev_JavaScript",
            "min_salary": 500,
            "max_salary": 1800,
            "date_posted": "2011-03-18"
        },
    ]

    criteria = "max_salary"
    sort_by(listJobs, criteria)
    assert listJobs[0]["max_salary"] == "7000"
    assert listJobs[1]["max_salary"] == "6000"
    assert listJobs[2]["max_salary"] == "3500"
    assert listJobs[3]["max_salary"] == "1800"

    criteria = "min_salary"
    sort_by(listJobs, criteria)
    assert listJobs[0]["min_salary"] == "500"
    assert listJobs[1]["min_salary"] == "600"
    assert listJobs[2]["min_salary"] == "1000"
    assert listJobs[3]["min_salary"] == "2000"

    criteria = "date_posted"
    sort_by(listJobs, criteria)
    assert listJobs[0]["date_posted"] == "2000-06-18"
    assert listJobs[1]["date_posted"] == "2008-09-15"
    assert listJobs[2]["date_posted"] == "2011-03-18"
    assert listJobs[3]["date_posted"] == "2020-10-21"
