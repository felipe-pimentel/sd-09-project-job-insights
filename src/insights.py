from src.jobs import read


def get_unique_job_types(path):
    list_of_jobs = read(path)
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """

    collection_jobs = set()
    for job in list_of_jobs:
        collection_jobs.add(job["job_type"])
    return collection_jobs


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    filtered_by_job_type = [job
                            for job in jobs
                            if job["job_type"] == job_type]
    return filtered_by_job_type


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
    list_of_industries = read(path)
    collection_industries = set()
    for industry in list_of_industries:
        if industry["industry"] not in collection_industries:
            if industry["industry"] != "":
                collection_industries.add(industry["industry"])
    return collection_industries


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

    """Seguindo exemplo do Course (filtro de restaurantes pela nota deles):
    Quando uma lista for criada por resultado de um for,
    pode-se usar a compreensão de listas
    """
    filtered_by_industry = [job
                            for job in jobs
                            if job["industry"] == industry]
    return filtered_by_industry


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    list_of_salaries = read(path)
    collection_salaries = set()
    for j_salary in list_of_salaries:
        if j_salary["max_salary"] != "" and j_salary["max_salary"].isnumeric():
            collection_salaries.add(int(j_salary["max_salary"]))
    return max(collection_salaries)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    list_of_salaries = read(path)
    collection_salaries = set()
    for j_salary in list_of_salaries:
        if j_salary["min_salary"] != "" and j_salary["min_salary"].isnumeric():
            collection_salaries.add(int(j_salary["min_salary"]))
    return min(collection_salaries)


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
