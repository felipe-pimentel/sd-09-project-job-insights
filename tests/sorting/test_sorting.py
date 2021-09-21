from src.sorting import sort_by


def test_sort_by_criteria():
    job_one = {
        "job_name": "job 1",
        "min_salary": 10000,
        "max_salary": 20000,
        "date_posted": "2021-09-21",
    }
    job_two = {
        "job_name": "job 2",
        "min_salary": 20000,
        "max_salary": 30000,
        "date_posted": "2021-09-21",
    }
    job_three = {
        "job_name": "job 3",
        "min_salary": 30000,
        "max_salary": 40000,
        "date_posted": "2021-09-21",
    }
    job_four = {
        "job_name": "job 4",
        "min_salary": 40000,
        "max_salary": 50000,
        "date_posted": "2021-09-21",
    }

    jobs_list = [job_one, job_two, job_three, job_four]
    min_salary = [job_one, job_two, job_three, job_four]
    max_salary = [job_four, job_three, job_two, job_one]
    date_posted = [job_four, job_three, job_two, job_one]

    sort_by(jobs_list, "min_salary")
    assert jobs_list == min_salary

    sort_by(jobs_list, "max_salary")
    assert jobs_list == max_salary

    sort_by(jobs_list, "date_posted")
    assert jobs_list == date_posted
