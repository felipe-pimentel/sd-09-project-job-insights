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

    all_jobs = read(path)
    unique_jobs = set()
    for job in all_jobs:
        unique_jobs.add(job["job_type"])
    data = list(unique_jobs)
    return data


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
    job_filtered = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_filtered.append(job)
    return job_filtered


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
    industries = read(path)
    unique_industries = set()
    for industry in industries:
        if industry["industry"]:
            unique_industries.add(industry["industry"])
    data = list(unique_industries)
    return data


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
    filtered_industry = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_industry.append(job)
    return filtered_industry


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
    data = read(path)
    max_salary = 0
    for salary in data:
        try:
            sal = int(salary["max_salary"])
        except ValueError:
            sal = 0
        if sal > max_salary:
            max_salary = sal
    return max_salary


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
    data = read(path)
    salaries = []
    for salary in data:
        if salary["min_salary"] != "" and salary["min_salary"].isdigit():
            salaries.append(int(salary["min_salary"]))
    min_salary = min(salaries)
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
    max_salary_type = True if type(job.get("max_salary")) is not int else False
    min_salary_type = True if type(job.get("min_salary")) is not int else False
    salary_type = True if type(salary) is not int else False

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    if max_salary_type or min_salary_type or salary_type:
        raise ValueError
    if job["min_salary"] > job["max_salary"]:
        raise ValueError
    if job["max_salary"] < 0 or job["min_salary"] < 0:
        raise ValueError
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
    jobs_filtered = []
    for job in jobs:
        try:
            range_salary = matches_salary_range(job, salary)
            if range_salary:
                jobs_filtered.append(job)
        except ValueError:
            pass
    return jobs_filtered
