from src.jobs import read


def get_unique_job_types(path):
    job_type = []
    jobs = read(path)
    for job in jobs:
        if not job["job_type"] in job_type:
            job_type.append(job["job_type"])
    return job_type


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    job_industry = []
    jobs = read(path)
    for job in jobs:
        if job["industry"] != "" and not job["industry"] in job_industry:
            job_industry.append(job["industry"])
    return job_industry


def filter_by_industry(jobs, industry):
    filtered_industry = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_industry.append(job)
    return filtered_industry


def get_max_salary(path):
    jobs = read(path)
    max_salary = 0
    for job in jobs:
        if (
            job["max_salary"] != ""
            and job["max_salary"] != "invalid"
            and int(job["max_salary"]) > max_salary
        ):
            max_salary = int(job["max_salary"])
    return max_salary


def get_min_salary(path):
    jobs = read(path)
    min_salary = 10000000000000000
    for job in jobs:
        if (
            job["min_salary"] != ""
            and job["min_salary"] != "invalid"
            and int(job["min_salary"]) < min_salary
        ):
            min_salary = int(job["min_salary"])
    return min_salary


def keys(job):
    if (
        'max_salary' in job and
        'min_salary' in job
       ):
        return True
    else:
        raise ValueError('erro')


def invalid_salary(job):
    if (
        type(job['max_salary']) == int and
        type(job['min_salary']) == int
       ):
        return True
    else:
        raise ValueError('erro')


def min_and_max(job):
    if job['max_salary'] > job['min_salary']:
        return True
    else:
        raise ValueError('erro')


def int_salary(salary):
    if type(salary) == int:
        return True
    else:
        raise ValueError('erro')


def matches_salary_range(job, salary):
    if (
        keys(job) and
        invalid_salary(job) and
        min_and_max(job) and
        int_salary(salary)
       ):
        return (job['min_salary'] <= salary <= job['max_salary'])
""" def matches_salary_range(job, salary):
    if 'max_salary' not in job and 'min_salary' not in job:
        raise ValueError('error')
    if type(job['max_salary']) != int and type(job['min_salary']) != int:
        raise ValueError('error')
    if job['max_salary'] < job['min_salary']:
        raise ValueError('error')
    if type(salary) != int:
        raise ValueError('error')
    return job['min_salary'] < salary < job['max_salary']
"""


def filter_by_salary_range(jobs, salary):
    accepts_salarys = []
    for job in jobs:
        try:
            matches_salary_range(job, salary)
        except ValueError:
            pass
        else:
            if matches_salary_range(job, salary):
                accepts_salarys.append(job)
    return accepts_salarys
