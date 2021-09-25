from src.sorting import sort_by


jobs = [
    {"min_salary": 100, "max_salary": 600, "date_posted": "01-01-2021"},
    {"min_salary": 200, "max_salary": 700, "date_posted": "02-02-2021"},
    {"min_salary": 300, "max_salary": 800, "date_posted": "03-03-2021"},
    {"min_salary": 400, "max_salary": 900, "date_posted": "04-04-2021"},
    {"min_salary": 500, "max_salary": 1000, "date_posted": "05-05-2021"},
]


def test_sort_by_criteria():

    expected_min_salary = [100, 200, 300, 400, 500]
    expected_max_salary = [1000, 900, 800, 700, 600]
    expected_date = [
        "05-05-2021",
        "04-04-2021",
        "03-03-2021",
        "02-02-2021",
        "01-01-2021"
    ]

    sort_by(jobs, "min_salary")
    assert [job["min_salary"] for job in jobs] == expected_min_salary

    sort_by(jobs, "max_salary")
    assert [job["max_salary"] for job in jobs] == expected_max_salary

    sort_by(jobs, "date_posted")
    assert [job["date_posted"] for job in jobs] == expected_date
