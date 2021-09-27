from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"max_salary": 0, "min_salary": 10, "date_posted": "2021-09-26"},
        {"max_salary": 10, "min_salary": 100, "date_posted": "2021-09-25"},
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2021-09-24"},
        {"max_salary": 15000, "min_salary": 0, "date_posted": "2021-09-23"},
        {"max_salary": 1500, "min_salary": 0, "date_posted": "2021-09-22"},
    ]

    expected_min_salary_order = [
        {"max_salary": 15000, "min_salary": 0, "date_posted": "2021-09-23"},
        {"max_salary": 1500, "min_salary": 0, "date_posted": "2021-09-22"},
        {"max_salary": 0, "min_salary": 10, "date_posted": "2021-09-26"},
        {"max_salary": 10, "min_salary": 100, "date_posted": "2021-09-25"},
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2021-09-24"},
    ]

    expected_max_salary_order = [
        {"max_salary": 15000, "min_salary": 0, "date_posted": "2021-09-23"},
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2021-09-24"},
        {"max_salary": 1500, "min_salary": 0, "date_posted": "2021-09-22"},
        {"max_salary": 10, "min_salary": 100, "date_posted": "2021-09-25"},
        {"max_salary": 0, "min_salary": 10, "date_posted": "2021-09-26"},
    ]

    expected_date_posted_order = [
        {"max_salary": 0, "min_salary": 10, "date_posted": "2021-09-26"},
        {"max_salary": 10, "min_salary": 100, "date_posted": "2021-09-25"},
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2021-09-24"},
        {"max_salary": 15000, "min_salary": 0, "date_posted": "2021-09-23"},
        {"max_salary": 1500, "min_salary": 0, "date_posted": "2021-09-22"},
    ]

    sort_by(jobs, "min_salary")
    assert jobs == expected_min_salary_order

    sort_by(jobs, "max_salary")
    assert jobs == expected_max_salary_order

    sort_by(jobs, "date_posted")
    assert jobs == expected_date_posted_order
