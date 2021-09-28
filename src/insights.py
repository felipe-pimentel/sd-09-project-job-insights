from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    jobs_type = set()

    for job in jobs:
        jobs_type.add(job["job_type"]),

    return [*jobs_type]


def filter_by_job_type(jobs, job_type):
    jobs_filtered = []
    for job in jobs:
        if (job['job_type'] == job_type):
            jobs_filtered.append(job)
  
    return jobs_filtered


def get_unique_industries(path):
    jobs = read(path)
    industries_types = set()
    for job in jobs:
        if job['industry'] != "":
            industries_types.add(job["industry"]),
    return [*industries_types]


def filter_by_industry(jobs, industry):
    industries_filtered = []
    for job in jobs:
        if (job['industry'] == industry):
            industries_filtered.append(job)

    return industries_filtered


def get_max_salary(path):
    jobs = read(path)
    salarys = []
    for job in jobs:
        if job["max_salary"].isnumeric():
            salarys.append(int(job['max_salary']))

    return max(salarys)


def get_min_salary(path):
    jobs = read(path)
    salarys = []
    for job in jobs:
        if job["min_salary"].isnumeric():
            salarys.append(int(job['min_salary']))

    return min(salarys)


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
    min_salary, max_salary = job.get('min_salary'), job.get('max_salary')
    if (type(min_salary or max_salary or salary) != int):
        raise ValueError
    if (min_salary > max_salary):
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
    jobs_filtered_by_salary = []

    for job in jobs:
        if (
            type(salary) is int
            and int(job["min_salary"]) <= int(job["max_salary"])
            and matches_salary_range(job, salary)
        ):
            jobs_filtered_by_salary.append(job)

    return jobs_filtered_by_salary
