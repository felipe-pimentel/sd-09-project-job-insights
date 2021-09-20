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
    all_jobs_types = set()
    for job in jobs:
        all_jobs_types.add(job["job_type"])

    return all_jobs_types


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
    # https://www.digitalocean.com/community/tutorials/how-to-use-the-python-filter-function-pt
    # Resolução com filter lambda
    # filter(lambda job: job["job_type"] == job_type, jobs)
    # Resolução com for e if
    # [job for job in jobs if job["job_type"] == job_type]
    return [job for job in jobs if job["job_type"] == job_type]


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
    all_industries = set()
    for job in jobs:
        if job["industry"]:
            all_industries.add(job["industry"])

    return all_industries


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
    return list(filter(lambda job: job["industry"] == industry, jobs))


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
    all_max_salary = set()
    for job in jobs:
        if job["max_salary"].isnumeric():
            all_max_salary.add(int(job["max_salary"]))

    max_salary = sorted(all_max_salary)
    return max_salary[-1]


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
    all_min_salary = set()
    for job in jobs:
        if job["min_salary"].isnumeric():
            all_min_salary.add(int(job["min_salary"]))

    min_salary = sorted(all_min_salary)
    return min_salary[0]


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
    if not ("min_salary" in job.keys() and "max_salary" in job.keys()):
        raise ValueError("min_salary and max_salary is not keys")
    # https://pt.stackoverflow.com/questions/176525/como-posso-saber-se-a-vari%C3%A1vel-%C3%A9-um-n%C3%BAmero-inteiro-em-python
    if not (
        isinstance(job["min_salary"], int)
        and isinstance(job["max_salary"], int)
    ):
        raise ValueError("min_salary and max_salary is not int")
    if not (
        job["min_salary"] >= 0
        and job["max_salary"] >= 0
    ):
        raise ValueError("min_salary and max_salary is not greater than zero")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary is greater than max_salary")
    return job["min_salary"] <= salary <= job["max_salary"]


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
    filtered_jobs = []
    for job in jobs:
        if (
            isinstance(salary, int)
            and ("min_salary" in job.keys() and "max_salary" in job.keys())
            and (job["min_salary"] >= 0 and job["max_salary"] >= 0)
            and job["min_salary"] <= job["max_salary"]
            and matches_salary_range(job, salary)
        ):
            filtered_jobs.append(job)
    return filtered_jobs
