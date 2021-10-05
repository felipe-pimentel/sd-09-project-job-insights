from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    unique_jobs_list = []
    for job in jobs_list:
        if job['job_type'] not in unique_jobs_list:
            unique_jobs_list.append(job['job_type'])
    return unique_jobs_list


def filter_by_job_type(jobs, job_type):
    jobs_by_type = []
    for job in jobs:
        if job['job_type'] == job_type:
            jobs_by_type.append(job)
    return jobs_by_type


def get_unique_industries(path):
    jobs_list = read(path)
    industries_list = []
    for job in jobs_list:
        if job['industry'] not in industries_list and job['industry'] != '':
            industries_list.append(job['industry'])
    return industries_list


def filter_by_industry(jobs, industry):
    industries_by_type = []
    for job in jobs:
        if job['industry'] == industry:
            industries_by_type.append(job)
    return industries_by_type


def get_max_salary(path):
    jobs_list = read(path)
    max_salary = 0
    for job in jobs_list:
        if job['max_salary'].isdigit() and int(job['max_salary']) > max_salary:
            max_salary = int(job['max_salary'])
    return max_salary


def get_min_salary(path):
    jobs_list = read(path)
    min_salary = get_max_salary(path)
    for job in jobs_list:
        if job['min_salary'].isdigit() and int(job['min_salary']) < min_salary:
            min_salary = int(job['min_salary'])
    return min_salary


def matches_salary_range(job, salary):
    if 'max_salary' not in job or 'min_salary' not in job:
        raise ValueError('ValueError exception thrown')
    if (type(job['min_salary']) != int or type(job['max_salary']) != int or
            type(salary) != int):
        raise ValueError('ValueError exception thrown')
    if job['min_salary'] > job['max_salary']:
        raise ValueError('ValueError exception thrown')
    if job['min_salary'] <= salary <= job['max_salary']:
        return True
    return False


def filter_by_salary_range(jobs, salary):
    jobs_salary_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_salary_range.append(job)
        except ValueError:
            print('ValueError')
    return jobs_salary_range
