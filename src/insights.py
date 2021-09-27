from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    jobs_type = set()
    for job in jobs_list:
        jobs_type.add(job['job_type'])

    return jobs_type


def filter_by_job_type(jobs, job_type):
    selected_jobs = []
    for job in jobs:
        if job['job_type'] == job_type:
            selected_jobs.append(job)

    return selected_jobs


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    return []


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    all_salaries = []
    jobs_list = read(path)
    for job in jobs_list:
        if job['max_salary'] != '' and job['max_salary'] != 'invalid':
            all_salaries.append(int(job['max_salary']))

    max_salary = max(all_salaries)
    return max_salary


def get_min_salary(path):
    all_salaries = []
    jobs_list = read(path)
    for job in jobs_list:
        if job['min_salary'] != '' and job['min_salary'] != 'invalid':
            all_salaries.append(int(job['min_salary']))

    min_salary = min(all_salaries)
    return min_salary


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
