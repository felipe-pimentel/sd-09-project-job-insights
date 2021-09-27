from src.sorting import sort_by


jobs = [
    {
        "title": "Web developer",
        "min_salary": "1000",
        "max_salary": "9000",
        "date_posted": "2019-10-11",
    },
    {
        "title": "Front end developer",
        "min_salary": "1500",
        "max_salary": "10000",
        "date_posted": "2019-10-12",
    },
    {
        "title": "Back end developer",
        "min_salary": "2000",
        "max_salary": "3000",
        "date_posted": "2019-10-13",
    },
    {
        "title": "Full stack end developer",
        "min_salary": "4000",
        "max_salary": "8000",
    },
]

jobs_min_salary = [jobs[0], jobs[1], jobs[2], jobs[3]]

jobs_max_salary = [jobs[1], jobs[0], jobs[3], jobs[2]]

jobs_by_date = [jobs[2], jobs[1], jobs[0], jobs[3]]

jobs_by = [jobs[2], jobs[1], jobs[0], jobs[3]]


def test_sort_by_criteria():
    assert sort_by(jobs, "min_salary") == jobs_min_salary
    assert sort_by(jobs, "max_salary") == jobs_max_salary
    assert sort_by(jobs, "date_posted") == jobs_by_date
    assert sort_by(jobs, "data_posted") == jobs_by
