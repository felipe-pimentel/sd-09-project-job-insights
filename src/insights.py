from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    jobs_around = set()
    for jobs in jobs_list:
        jobs_around.add(jobs["job_type"])
    return jobs_around


def filter_by_job_type(jobs, job_type):
    job_list = []
    for job in jobs:
        if (job['job_type'] == job_type):
            job_list.append(job)
    return job_list


def get_unique_industries(path):
    jobs_list = read(path)
    jobs_around = set()
    for jobs in jobs_list:
        if (jobs['industry'] != ''):
            jobs_around.add(jobs['industry'])
    return jobs_around


def filter_by_industry(jobs, industry):
    job_list = []
    for job in jobs:
        if (job['industry'] == industry):
            job_list.append(job)
    return job_list


def get_max_salary(path):
    jobs_list = read(path)
    jobs_around = set()
    for jobs in jobs_list:
        if (jobs['max_salary'].isdigit()):
            jobs_around.add(int(jobs['max_salary']))
    job_max_value = max(jobs_around, key=int)
    return job_max_value


def get_min_salary(path):
    jobs_list = read(path)
    jobs_around = set()
    for jobs in jobs_list:
        if (jobs['min_salary'].isdigit()):
            jobs_around.add(int(jobs['min_salary']))
    job_min_value = min(jobs_around, key=int)
    return job_min_value


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
