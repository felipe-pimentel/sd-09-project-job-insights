from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "id": 1,
            "min_salary": 1000,
            "max_salary": 2000,
            "date_posted": "1990-01-01",
        },
        {
            "id": 2,
            "min_salary": 2500,
            "max_salary": 4500,
            "date_posted": "1997-07-17",
        },
        {
            "id": 3,
            "min_salary": 3000,
            "max_salary": 6000,
            "date_posted": "1997-12-20",
        },
    ]
    sorted_min_wage = [jobs[0], jobs[1], jobs[2]]
    sorted_max_wage = [jobs[2], jobs[1], jobs[0]]
    sorted_date_posted = [jobs[2], jobs[1], jobs[0]]

    sort_by(jobs, "min_salary")
    assert jobs == sorted_min_wage
    sort_by(jobs, "max_salary")
    assert jobs == sorted_max_wage
    sort_by(jobs, "date_posted")
    assert jobs == sorted_date_posted
