# from jobs import read

from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)

    types = set()
    for row in jobs_list:
        types.add(row["job_type"])

    return types


def filter_by_job_type(jobs, job_type):
    jobs_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_list.append(job)

    return jobs_list


def get_unique_industries(path):
    list = read(path)

    industries = set()
    for row in list:
        if row["industry"]:
            industries.add(row["industry"])

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
    list_salary = read(path)

    salary = 0
    for row in list_salary:
        if row["max_salary"].isnumeric() and int(row["max_salary"]) > salary:
            salary = int(row["max_salary"])

    return salary


def get_min_salary(path):
    list_salary = read(path)

    salary = 9999999
    for row in list_salary:
        if row["min_salary"].isnumeric() and int(row["min_salary"]) < salary:
            salary = int(row["min_salary"])

    return salary


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
