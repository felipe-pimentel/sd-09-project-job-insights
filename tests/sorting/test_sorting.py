from src.sorting import sort_by
from datetime import date

# mock_jobs
jobs = [
    {"max_salary": 10000, "min_salary": 2000, "date_posted": "2021-09-23"},
    {"max_salary": 15000, "min_salary": 3000, "date_posted": "2021-09-15"},
    {"max_salary": 16000, "min_salary": 4000, "date_posted": "2021-09-10"},
    {"max_salary": 7000, "min_salary": 5000, "date_posted": "2021-09-02"},
    {"max_salary": 30000, "min_salary": 10000, "date_posted": "2021-09-19"},
]


def test_sort_by_criteria():
    expected_max_salary = [30000, 16000, 15000, 10000, 7000]
    expected_min_salary = [2000, 3000, 4000, 5000, 10000]
    expected_date_posted = [
        date.fromisoformat("2021-09-23"),
        date.fromisoformat("2021-09-19"),
        date.fromisoformat("2021-09-15"),
        date.fromisoformat("2021-09-10"),
        date.fromisoformat("2021-09-02"),
    ]

    assert sort_by(jobs, "max_salary") == expected_max_salary
    assert sort_by(jobs, "min_salary") == expected_min_salary
    assert sort_by(jobs, "date_posted") == expected_date_posted
