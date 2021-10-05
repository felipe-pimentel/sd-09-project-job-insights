from src.sorting import sort_by

jobs_list = [
    {"min_salary": 1, "max_salary": 6, "date_posted": "05-11-2010"},
    {"min_salary": 2, "max_salary": 7, "date_posted": "08-11-2010"},
    {"min_salary": 3, "max_salary": 8, "date_posted": "06-11-2010"},
    {"min_salary": 4, "max_salary": 9, "date_posted": "04-11-2010"},
]


def test_sort_by_criteria():
    sort_by(jobs_list, "max_salary")
    assert [job["max_salary"] for job in jobs_list] == [9, 8, 7, 6]

    sort_by(jobs_list, "min_salary")
    assert [job["min_salary"] for job in jobs_list] == [1, 2, 3, 4]

    sort_by(jobs_list, "date_posted")
    assert [job["date_posted"] for job in jobs_list] == [
        "05-11-2010",
        "08-11-2010",
        "06-11-2010",
        "04-11-2010",
      ]
