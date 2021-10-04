from src.sorting import sort_by


def test_sort_by_criteria():
    list_jobs = [
        {
            "job_function": "Fullstack",
            "min_salary": "3000",
            "max_salary": "8000",
            "date_posted": "27-09-2021",
        },
        {
            "job_function": " Front-End",
            "min_salary": "4000",
            "max_salary": "10000",
            "date_posted": "28-09-2018",
        },
        {
            "job_function": " Back-end",
            "min_salary": "5000",
            "max_salary": "12000",
            "date_posted": "30-09-2009",
        },
    ]

    min_salary = [
        list_jobs[0],
        list_jobs[1],
        list_jobs[2],
    ]

    max_salary = [
        list_jobs[2],
        list_jobs[1],
        list_jobs[0],
    ]

    date_jobs_list = [
        list_jobs[2],
        list_jobs[1],
        list_jobs[0],
    ]

    sort_by(list_jobs, "min_salary")
    assert list_jobs == min_salary, "não esta igual a min_salary"

    sort_by(list_jobs, "max_salary")
    assert list_jobs == max_salary, "não esta igual a max_salary"

    sort_by(list_jobs, 'date_posted')
    assert list_jobs == date_jobs_list, "não esta igual a date_jobs_list"
