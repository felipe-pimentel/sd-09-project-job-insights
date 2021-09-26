from src.sorting import sort_by


def test_sort_by_criteria():
    job_one = {
        'id_': 1,
        'min_salary': 1200,
        'max_salary': 3000,
        'date_posted': '01-01-2000'
    }
    job_two = {
        'id_': 2,
        'min_salary': 2000,
        'max_salary': 3500,
        'date_posted': '05-05-2000'
    }
    job_three = {
        'id_': 3,
        'min_salary': 3000,
        'max_salary': 4000,
        'date_posted': '07-07-2000'
    }
    job_four = {
        'id_': 4,
        'min_salary': 3500,
        'max_salary': 4500,
        'date_posted': '10-10-2000'
    }
    jobs_list = [job_one, job_two, job_three, job_four]
    min_jobs_list = [job_one, job_two, job_three, job_four]
    mxm_jobs_list = [job_four, job_three, job_two, job_one]
    date_jobs_list = [job_four, job_three, job_two, job_one]

    sort_by(jobs_list, 'min_salary')
    assert jobs_list == min_jobs_list

    sort_by(jobs_list, 'max_salary')
    assert jobs_list == mxm_jobs_list

    sort_by(jobs_list, 'date_posted')
    assert jobs_list == date_jobs_list
