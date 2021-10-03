from src.jobs import read


def get_unique_job_types(path):
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
    jobs = read(path)
    all_jobs_type = []

    for job in jobs:
        all_jobs_type.append(job["job_type"])

    return list(set(all_jobs_type))


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
    filter_jobs = []

    for job in jobs:
        if job["job_type"] == job_type:
            filter_jobs.append(job)

    return filter_jobs


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
    jobs = read(path)
    all_industries = []

    for job in jobs:
        if len(job["industry"]) > 0:
            all_industries.append(job["industry"])

    return list(set(all_industries))


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
    filter_industry = []

    for job in jobs:
        if job["industry"] == industry:
            filter_industry.append(job)

    return filter_industry


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
    jobs = read(path)
    all_max_salary = []

    for job in jobs:
        if len(job["max_salary"]) > 0 and job["max_salary"].isnumeric():
            all_max_salary.append(int(job["max_salary"]))

    return max(all_max_salary)


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
    jobs = read(path)
    all_min_salary = []

    for job in jobs:
        if len(job["min_salary"]) > 0 and job["min_salary"].isnumeric():
            all_min_salary.append(int(job["min_salary"]))

    return min(all_min_salary)


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
    # dict.get(key) => Documentacao Python
    # Retorna o valor para key se key está no dicionário, caso contrário
    # "default". Se default não é fornecido, será usado o valor padrão "None",
    # de tal forma que este método nunca levanta um KeyError.
    min_salary, max_salary = job.get("min_salary"), job.get("max_salary")

    if (
        # not min_salary
        # or not max_salary
        type(min_salary) != int
        or type(max_salary) != int
        or min_salary > max_salary
        or type(salary) != int
    ):
        raise ValueError

    return min_salary <= salary <= max_salary


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
    filter_salary = []

    for job in jobs:
        max_salary, min_salary = job.get("max_salary"), job.get("min_salary")

        if (
            type(min_salary) == int
            and type(max_salary) == int
            and type(salary) == int
            and min_salary < max_salary
            and min_salary <= salary <= max_salary
        ):
            filter_salary.append(job)

    return filter_salary
