from src.sorting import sort_by

jobs = [
    {
        "min_salary": 1500,
        "max_salary": 8500,
        "date_posted": "01-08-2021"
    },
    {
        "min_salary": 2000,
        "max_salary": 10500,
        "date_posted": "05-04-2021"
    },
    {
        "min_salary": 4500,
        "max_salary": 15000,
        "date_posted": "22-09-2021"
    },
]


def test_sort_by_criteria():
    expected_date = [
        "22-09-2021",
        "05-04-2021",
        "01-08-2021"]

    sort_by(jobs, "min_salary")
    assert [job["min_salary"] for job in jobs] == [1500, 2000, 4500]

    sort_by(jobs, "max_salary")
    assert [job["max_salary"] for job in jobs] == [15000, 10500, 8500]

    sort_by(jobs, "date_posted")
    assert [job["date_posted"] for job in jobs] == expected_date
