from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"max_salary": 100, "min_salary": 10, "date_posted": "2021-09-29"},
        {"max_salary": 200, "min_salary": 100, "date_posted": "2021-09-18"},
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2021-08-29"},
        {"max_salary": 15000, "min_salary": 1200, "date_posted": "2021-09-11"},
        {"max_salary": 1500, "min_salary": 700, "date_posted": "2021-09-21"}
    ]

    expected_min_salary_order = [
        {"max_salary": 100, "min_salary": 10, "date_posted": "2021-09-29"},
        {"max_salary": 200, "min_salary": 100, "date_posted": "2021-09-18"},
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2021-08-29"},
        {"max_salary": 1500, "min_salary": 700, "date_posted": "2021-09-21"},
        {"max_salary": 15000, "min_salary": 1200, "date_posted": "2021-09-11"},
    ]

    expected_max_salary_order = [
        {"max_salary": 15000, "min_salary": 1200, "date_posted": "2021-09-11"},
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2021-08-29"},
        {"max_salary": 1500, "min_salary": 700, "date_posted": "2021-09-21"},
        {"max_salary": 200, "min_salary": 100, "date_posted": "2021-09-18"},
        {"max_salary": 100, "min_salary": 10, "date_posted": "2021-09-29"},
    ]

    expected_date_posted_order = [
        {"max_salary": 100, "min_salary": 10, "date_posted": "2021-09-29"},
        {"max_salary": 1500, "min_salary": 700, "date_posted": "2021-09-21"},
        {"max_salary": 200, "min_salary": 100, "date_posted": "2021-09-18"},
        {"max_salary": 15000, "min_salary": 1200, "date_posted": "2021-09-11"},
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2021-08-29"},
    ]

    sort_by(jobs, "min_salary")
    assert jobs == expected_min_salary_order

    sort_by(jobs, "max_salary")
    assert jobs == expected_max_salary_order

    sort_by(jobs, "date_posted")
    assert jobs == expected_date_posted_order
