from src.sorting import sort_by


jobs = [
    {"max_salary": 8000, "min_salary": 1000, "date_posted": "2019-07-03"},
    {"max_salary": 1700, "min_salary": 0, "date_posted": "2020-09-04"},
    {"max_salary": 2000, "min_salary": 1200, "date_posted": "2021-02-02"},
]

max = [jobs[0], jobs[2], jobs[1]]
min = [jobs[1], jobs[2], jobs[0]]
date = [jobs[2], jobs[1], jobs[0]]


def test_sort_by_criteria():
    sort_by(jobs, "max_salary")
    assert jobs == max

    sort_by(jobs, "min_salary")
    assert jobs == min

    sort_by(jobs, "date_posted")
    assert jobs == date
