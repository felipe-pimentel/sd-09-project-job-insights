from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "title": "Frontend dev",
            "min_salary": "2000",
            "max_salary": "6000",
            "date_posted": "2020-04-12",
        },
        {
            "title": "Fullstack dev",
            "min_salary": "4000",
            "max_salary": "8000",
            "date_posted": "2020-01-01",
        },
        {
            "title": "Backend dev",
            "min_salary": "3000",
            "max_salary": "7000",
            "date_posted": "2021-04-03",
        },
    ]
    assert sort_by(jobs, 'min_salary') == [
        {
            "title": "Frontend dev",
            "min_salary": "2000",
            "max_salary": "6000",
            "date_posted": "2020-04-12",
        },
        {
            "title": "Backend dev",
            "min_salary": "3000",
            "max_salary": "7000",
            "date_posted": "2021-04-03",
        },
        {
            "title": "Fullstack dev",
            "min_salary": "4000",
            "max_salary": "8000",
            "date_posted": "2020-01-01",
        },
    ]
    assert sort_by(jobs, 'date_posted') == [
        {
            "title": "Frontend dev",
            "min_salary": "2000",
            "max_salary": "6000",
            "date_posted": "2020-04-12",
        },
        {
            "title": "Backend dev",
            "min_salary": "3000",
            "max_salary": "7000",
            "date_posted": "2021-04-03",
        },
        {
            "title": "Fullstack dev",
            "min_salary": "4000",
            "max_salary": "8000",
            "date_posted": "2020-01-01",
        },
    ]
