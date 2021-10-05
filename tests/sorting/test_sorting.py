from src.sorting import sort_by

all_jobs = [
    {
        "min_salary": 2000,
        "max_salary": 4000,
        "date_posted": "04-10-2021",
    },
    {
        "min_salary": 1000,
        "max_salary": 2000,
        "date_posted": "03-10-2021",
    },
    {
        "min_salary": 3000,
        "max_salary": 6000,
        "date_posted": "05-10-2021",
    },
]

jobs_by_max_salary = [
    {
        "min_salary": 1000,
        "max_salary": 2000,
        "date_posted": "03-10-2021",
    },
    {
        "min_salary": 2000,
        "max_salary": 4000,
        "date_posted": "04-10-2021",
    },
    {
        "min_salary": 3000,
        "max_salary": 6000,
        "date_posted": "05-10-2021",
    },
]

jobs_by_min_salary = [
    {
        "min_salary": 1000,
        "max_salary": 2000,
        "date_posted": "03-10-2021",
    },
    {
        "min_salary": 2000,
        "max_salary": 4000,
        "date_posted": "04-10-2021",
    },
    {
        "min_salary": 3000,
        "max_salary": 6000,
        "date_posted": "05-10-2021",
    },
]

jobs_by_date_posted = [
    {
        "min_salary": 3000,
        "max_salary": 6000,
        "date_posted": "05-10-2021",
    },
    {
        "min_salary": 2000,
        "max_salary": 4000,
        "date_posted": "04-10-2021",
    },
    {
        "min_salary": 1000,
        "max_salary": 2000,
        "date_posted": "03-10-2021",
    },
]


def test_sort_by_criteria():
    assert sort_by(all_jobs, "max_salary") == jobs_by_max_salary

    assert sort_by(all_jobs, "min_salary") == jobs_by_min_salary

    assert sort_by(all_jobs, "date_posted") == jobs_by_date_posted
