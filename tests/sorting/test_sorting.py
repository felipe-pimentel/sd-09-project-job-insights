from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"id": 1,
         "min_salary": 500,
         "max_salary": 1000,
         "date_posted": "2020-05-07"},
        {"id": 2,
         "min_salary": 300,
         "max_salary": 3000,
         "date_posted": "2020-05-08"},
        {"id": 3,
         "min_salary": 100,
         "max_salary": 150,
         "date_posted": "2020-05-06"},
    ]

    sorted_jobs_min_salary = [
            {"id": 3,
             "min_salary": 100,
             "max_salary": 150,
             "date_posted": "2020-05-06"},
            {"id": 2,
             "min_salary": 300,
             "max_salary": 3000,
             "date_posted": "2020-05-08"},
            {"id": 1,
             "min_salary": 500,
             "max_salary": 1000,
             "date_posted": "2020-05-07"},
        ]

    sort_by(jobs, "min_salary")

    assert jobs == sorted_jobs_min_salary
