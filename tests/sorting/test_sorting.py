from src.sorting import sort_by


def test_sort_by_criteria():
    job_1 = {
        "job_title": "Web developer",
        "min_salary": 46000,
        "max_salary": 55000,
        "date_posted": "2021-10-18",
    }
    job_2 = {
        "job_title": "Front end developer",
        "min_salary": 55000,
        "max_salary": 75000,
        "date_posted": "2021-01-18",
    }
    job_3 = {
        "job_title": "Back end developer",
        "min_salary": 20000,
        "max_salary": 35000,
        "date_posted": "2021-04-27",
    }
    job_4 = {
        "job_title": "Full stack developer",
        "min_salary": 44000,
        "max_salary": 85000,
        "date_posted": "2021-04-10",
    }
    jobs = [job_1, job_2, job_3, job_4]

    min_salary_sort = [job_3, job_4, job_1, job_2]
    max_salary_sort = [job_4, job_2, job_1, job_3]
    date_posted_sort = [job_1, job_3, job_4, job_2]
    
    criteria = ["min_salary", "max_salary", "date_posted"]
    expected = [min_salary_sort, max_salary_sort, date_posted_sort]

    # lembrar que esse método sort altera
    for index in range(len(criteria)):
        sort_by(jobs, criteria[index])  # muda o job_list
        assert jobs == expected[index]
