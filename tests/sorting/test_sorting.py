from src.sorting import sort_by


def test_sort_by_criteria():

    jobs = [
        {
            "id": 1,
            "date_posted": "09-11-2020",
            "max_salary": 1300,
            "min_salary": 1000,
        },
        {
            "id": 2,
            "date_posted": "12-03-1991",
            "max_salary": 5000,
            "min_salary": 2700,
        },
        {
            "id": 3,
            "date_posted": "09-02-2015",
            "max_salary": 3000,
            "min_salary": 1900,
        },
        {
            "id": 3,
            "date_posted": "08-08-2003",
            "max_salary": 1000,
            "min_salary": 800,
        },
    ]

    date_posted = [jobs[0], jobs[2], jobs[3], jobs[1]]
    max_salary = [jobs[1], jobs[2], jobs[0], jobs[3]]
    min_salary = [jobs[3], jobs[0], jobs[2], jobs[1]]

    criteria_keys = ["date_posted", "max_salary", "min_salary"]

    sort_by(jobs, criteria_keys[0])
    assert jobs != date_posted
    sort_by(jobs, criteria_keys[1])
    assert jobs == max_salary
    sort_by(jobs, criteria_keys[2])
    assert jobs == min_salary
