from src.sorting import sort_by


def test_sort_by_criteria():
    jobs_simulation = [
        {
            "min_salary": 3500,
            "max_salary": 7000,
            "date_posted": "2003-11-30",
        },
        {
            "min_salary": 2500,
            "max_salary": 4500,
            "date_posted": "2001-09-11",
        },
        {
            "min_salary": 4000,
            "max_salary": 6500,
            "date_posted": "1998-02-10",
        },
    ]

    min_salary = [
        jobs_simulation[1],
        jobs_simulation[0],
        jobs_simulation[2]
    ]
    max_salary = [
        jobs_simulation[1],
        jobs_simulation[2],
        jobs_simulation[0]
    ]
    posted_date_ordered = [
        jobs_simulation[0],
        jobs_simulation[1],
        jobs_simulation[2]
    ]

    sort_by(jobs_simulation, "min_salary")
    assert jobs_simulation == min_salary
    sort_by(jobs_simulation, "max_salary")
    assert jobs_simulation == max_salary
    sort_by(jobs_simulation, "date_posted")
    assert jobs_simulation == posted_date_ordered
