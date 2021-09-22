from src.sorting import sort_by

def test_sort_by_criteria():
    job_1 = {
        "job_name": "Developer",
        "min_salary": 35000,
        "max_salary": 55000,
        "date_posted": "2021-09-22",
    }
    job_2 = {
        "job_name": "Lawyer",
        "min_salary": 32000,
        "max_salary": 80000,
        "date_posted": "2021-09-21",
    }
    job_3 = {
        "job_name": "Electronic Engineer",
        "min_salary": 30000,
        "max_salary": 52000,
        "date_posted": "2021-09-20",
    }
    job_4 = {
        "job_name": "Doctor",
        "min_salary": 40000,
        "max_salary": 130000,
        "date_posted": "2021-09-19",
    }

    job_list = [job_1, job_2, job_3, job_4]

    min_salary_asc_sort = [job_3, job_2, job_1, job_4]
    max_salary_desc_sort = [job_4, job_2, job_1, job_3]  
    date_posted_desc_sort = [job_1, job_3, job_4, job_2]  

    criteria = ["min_salary", "max_salary", "date_posted"]
    expected = [min_salary_asc_sort, max_salary_desc_sort, date_posted_desc_sort]

    for index in range(len(criteria)):
        sort_by(job_list, criteria[index])
        assert job_list == expected[index]