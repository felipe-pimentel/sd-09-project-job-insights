from src.jobs import read


def get_unique_job_types(path):
    file = read(path)
    job_types = set()
    for row in file:
        job_types.add(row["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    job_list = []

    for job in jobs:
        if (job["job_type"] == job_type):
            job_list.append(job)
    return job_list


def get_unique_industries(path):
    file = read(path)
    industries = set()
    for row in file:
        if (row["industry"] != ''):
            industries.add(row["industry"])
    return industries


def filter_by_industry(jobs, industry):
    job_list = []

    for job in jobs:
        if (job["industry"] == industry):
            job_list.append(job)
    return job_list


def get_max_salary(path):
    file = read(path)
    salaries = set()
    for row in file:
        if(row["max_salary"].isdigit()):
            salaries.add(int(row['max_salary']))
    max_salary = max(salaries, key=int)
    return max_salary


def get_min_salary(path):
    file = read(path)
    salaries = set()
    for row in file:
        if(row["min_salary"].isdigit()):
            salaries.add(int(row['min_salary']))
    min_salary = min(salaries, key=int)
    return min_salary


def matches_salary_range(job, salary):
    if not (
        isinstance(job.get('min_salary'), int)
        or isinstance(job.get('max_salary'), int)
    ):
        raise ValueError('Problemas com tipo de min e max sal')
    if not isinstance(salary, int):
        raise ValueError('Problemas com tipo do salary')
    if (
        'min_salary' not in job
        or 'max_salary' not in job
    ):
        raise ValueError('Problemas com ausensia de min ou max sal')
    if job['min_salary'] > job['max_salary']:
        raise ValueError('Problemas com min maior que max')
    salary_check = int(job['min_salary']) <= salary <= int(job['max_salary'])

    return salary_check


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
