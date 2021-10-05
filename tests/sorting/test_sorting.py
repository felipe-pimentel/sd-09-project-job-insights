from src.sorting import sort_by


jobs = [
    {
        "min_salary": 1000,
        "max_salary": 2000,
        "date_posted": "2021-07-19"
    },
    {
        "min_salary": 3000,
        "max_salary": 4000,
        "date_posted": "2021-01-01"
    },
    {
        "min_salary": 5000,
        "max_salary": 6000,
        "date_posted": "2021-01-02"
    },
]

def test_sort_by_criteria():
    criteria = "min_salary"
    sort_by(jobs,criteria)
    assert jobs[0]["min_salary"] == 1000

    criteria = "max_salary"
    sort_by(jobs,criteria)
    assert jobs[0]["max_salary"] == 6000

    criteria = "date_posted"
    sort_by(jobs,criteria)
    assert jobs[0]["min_salary"] == "2021-07-19"