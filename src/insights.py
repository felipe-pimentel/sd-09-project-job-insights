from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    job_types = []

    for job in jobs:
        if job['job_type'] not in job_types:
            job_types.append(job['job_type'])
    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = [
        job for job in jobs
        if job['job_type'] == job_type
    ]
    return filtered_jobs


def get_unique_industries(path):
    jobs = read(path)
    job_industries = []

    for job in jobs:
        if job['industry'] not in job_industries and job['industry'] != '':
            job_industries.append(job['industry'])
    return job_industries


def filter_by_industry(jobs, industry):
    filtered_jobs = [
        job for job in jobs
        if job['industry'] == industry
    ]
    return filtered_jobs


def get_max_salary(path):
    jobs = read(path)
    max_salary = 0
    for job in jobs:
        if (
            job['max_salary'] != ''
            and job['max_salary'] != 'invalid'
            and int(job['max_salary']) > max_salary
           ):
            max_salary = int(job['max_salary'])
    return max_salary


def get_min_salary(path):
    jobs = read(path)
    min_salary = 100000000
    for job in jobs:
        if (
            job['min_salary'] != ''
            and job['min_salary'] != 'invalid'
            and int(job['min_salary']) < min_salary
           ):
            min_salary = int(job['min_salary'])
    return min_salary


def exist_salary_keys(job):
    if (
        'max_salary' in job and
        'min_salary' in job
       ):
        return True
    else:
        raise ValueError('Chaves inexsistentes')


def invalid_salary_types(job):
    if (
        type(job['max_salary']) == int and
        type(job['min_salary']) == int
       ):
        return True
    else:
        raise ValueError('Chaves não inteiras')


def incorrect_min_and_max(job):
    if job['max_salary'] > job['min_salary']:
        return True
    else:
        raise ValueError('Minimo e máximo incorretos')


def int_salary(salary):
    if type(salary) == int:
        return True
    else:
        raise ValueError('Salario não inteiro')


def matches_salary_range(job, salary):
    if (
        exist_salary_keys(job) and
        invalid_salary_types(job) and
        incorrect_min_and_max(job) and
        int_salary(salary)
       ):
        matche = job['min_salary'] <= salary <= job['max_salary']
    return matche


def filter_by_salary_range(jobs, salary):
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            pass
    return filtered_jobs
