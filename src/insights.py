from .jobs import read


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
    job_types = set()
    for job in jobs:
        job_types.add(job["job_type"])
    return job_types
# aqui vamos usar conjuntos (set) porque queremos
# elementos únicos e não ordenados


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
    filtered_jobs = [job
                     for job in jobs
                     if job["job_type"] == job_type]
    return filtered_jobs


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
    industries = set()
    for job in jobs:
        if job["industry"] != "":
            industries.add(job["industry"])
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
    jobs_filtered_by_industry = [job
                                 for job in jobs
                                 if job["industry"] == industry]
    return jobs_filtered_by_industry


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
    max_salaries = [int(job["max_salary"])
                    for job in jobs
                    if job["max_salary"] != ""
                    and job["max_salary"].isnumeric()]
    return max(max_salaries)


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
    min_salaries = [int(job["min_salary"])
                    for job in jobs
                    if job["min_salary"] != ""
                    and job["min_salary"].isnumeric()]
    return min(min_salaries)


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
    # dica do Rafa: declarar as variaveis para codigo mais limpo e
    # usar job.get("min_salary"), pq se nao existe, retorna null

    min_salary, max_salary = job.get("min_salary"), job.get("max_salary")
    # if "min_salary" not in job or "max_salary" not in job:

    if (
        type(min_salary) != int
        or type(max_salary) != int
        or type(salary) != int
        or min_salary > max_salary
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
    jobs_filtered_by_salary_range = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_filtered_by_salary_range.append(job)
        except ValueError:
            pass
    return jobs_filtered_by_salary_range
