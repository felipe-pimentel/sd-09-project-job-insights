from os import path, sep

from src.jobs import read

file_path = path.dirname(__file__) + sep + 'jobs.csv'


def get_unique_job_types(path):
    jobs_list = read(path)
    job_type_set = set()

    for job in jobs_list:
        job_type_set.add(job['job_type'])

    return job_type_set


def filter_by_job_type(jobs, job_type):
    job_list = []
    for job in jobs:
        if (job['job_type'] in job_type):
            job_list.append(job)

    return job_list


def get_unique_industries(path):
    jobs_list = read(path)
    industry_set = set()

    for job in jobs_list:
        if (job['industry'] != ''):
            industry_set.add(job['industry'])

    return industry_set


def filter_by_industry(jobs, industry):
    job_list = []
    for job in jobs:
        if (job['industry'] in industry):
            job_list.append(job)

    return job_list


def get_max_salary(path):
    jobs_list = read(path)
    salary_set = set()

    for job in jobs_list:
        if (job['max_salary'].isdigit()):
            salary_set.add(int(job['max_salary']))

    max_salary_value = max(salary_set, key=int)
    return max_salary_value


def get_min_salary(path):
    jobs_list = read(path)
    salary_set = set()

    for job in jobs_list:
        if (job['min_salary'].isdigit()):
            salary_set.add(int(job['min_salary']))

    min_salary_value = min(salary_set, key=int)
    return min_salary_value


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
