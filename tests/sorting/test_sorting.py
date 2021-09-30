from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "min_salary": 3500,
            "max_salary": 9000,
            "date_posted": "2020-09-09"
        },
        {
            "min_salary": 6500,
            "max_salary": 12000,
            "date_posted": "2020-08-09"
        },
        {
            "min_salary": 2500,
            "max_salary": 7000,
            "date_posted": "2020-07-09"
        }
    ]

    jobs_by_date = [jobs[0], jobs[1], jobs[2]]
    jobs_by_max_salary = [jobs[1], jobs[0], jobs[2]]
    jobs_by_min_salary = [jobs[2], jobs[0], jobs[1]]

    sort_by(jobs, 'min_salary')
    assert jobs == jobs_by_min_salary
    sort_by(jobs, 'max_salary')
    assert jobs == jobs_by_max_salary
    sort_by(jobs, 'date_posted')
    assert jobs == jobs_by_date
