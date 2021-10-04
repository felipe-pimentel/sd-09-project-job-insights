from src.sorting import sort_by


def test_sort_by_criteria():
    jobs_list = [
        {
            "max_salary": "2000",
            "min_salary": "1000",
            "date_posted": "2021-03-01",
        },
        {
            "max_salary": "4000",
            "min_salary": "2001",
            "date_posted": "2021-04-01",
        },
        {
            "max_salary": "6000",
            "min_salary": "4001",
            "date_posted": "2021-05-01"
        },
    ]

    criteria = "min_salary"
    sort_by(jobs_list, criteria)
    assert jobs_list[0]["min_salary"] == "1000"

    criteria = "max_salary"
    sort_by(jobs_list, criteria[1])
    assert jobs_list[0]["max_salary"] == "2000"

    criteria = "date_posted"
    sort_by(jobs_list, criteria[2])
    assert jobs_list[0]["date_posted"] == "2021-03-01"
