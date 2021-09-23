from src.sorting import sort_by


def test_sort_by_criteria():
    jobs_mock = [
        {
            "title": "Job 1",
            "min_salary": 1000,
            "max_salary": 2000,
            "date_posted": "2021-09-25",
        },
        {
            "title": "Job 2",
            "min_salary": 3000,
            "max_salary": 4000,
            "date_posted": "2021-09-13",
        },
        {
            "title": "Job 3",
            "min_salary": 9000,
            "max_salary": 10000,
            "date_posted": "2021-09-29",
        },
        {
            "title": "Job 4",
            "min_salary": 5000,
            "max_salary": 6000,
            "date_posted": "2021-09-30",
        },
        {
            "title": "Job 5",
            "min_salary": 7000,
            "max_salary": 8000,
            "date_posted": "2021-09-01",
        },
    ]

    highest_min = jobs_mock[2]
    highest_max = jobs_mock[2]
    lowest_min = jobs_mock[0]
    lowest_max = jobs_mock[0]
    latest_date = jobs_mock[3]
    earliest_date = jobs_mock[4]

    sort_by(jobs_mock, "min_salary")
    assert jobs_mock[0] == lowest_min
    assert jobs_mock[-1] == highest_min

    sort_by(jobs_mock, "max_salary")
    assert jobs_mock[0] == highest_max
    assert jobs_mock[-1] == lowest_max

    sort_by(jobs_mock, "date_posted")
    assert jobs_mock[0] == latest_date
    assert jobs_mock[-1] == earliest_date
