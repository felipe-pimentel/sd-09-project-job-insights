from src.jobs import read


def get_unique_job_types(path):
    returned_jobs = read(path)
    job_types = []
    for job in returned_jobs:
        if job["job_type"] != '':
            job_types.append(job["job_type"])
    job_types = list(dict.fromkeys(job_types))
    return job_types


def filter_by_job_type(jobs, job_type):
    found_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            found_jobs.append(job)
    return found_jobs


def get_unique_industries(path):
    returned_jobs = read(path)
    industries = []
    for job in returned_jobs:
        if job["industry"] != '':
            industries.append(job["industry"])
    industries = list(dict.fromkeys(industries))
    return industries


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
    returned_jobs = read(path)
    salaries = []
    for job in returned_jobs:
        try:
            if job["max_salary"] != '':
                salaries.append(int(job["max_salary"]))
        except ValueError:
            print("Valor não convertido")
    return max(salaries)


def get_min_salary(path):
    returned_jobs = read(path)
    salaries = []
    for job in returned_jobs:
        try:
            if job["min_salary"] != '':
                salaries.append(int(job["min_salary"]))
        except ValueError:
            print("Valor não convertido")
    return min(salaries)


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
