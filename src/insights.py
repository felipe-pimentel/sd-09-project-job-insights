from jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    job_types = set()
    for job in jobs_list:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    result = []
    for job in jobs:
        if job["job_type"] == job_type:
            result.append(job)
    return result


def get_unique_industries(path):
    jobs_list = read(path)
    industries = set()
    for job in jobs_list:
        industries.add(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    result = []
    for job in jobs:
        if job["industry"] == industry:
            result.append(job)
    return result


def get_max_salary(path):
    jobs = read(path)
    max_salaries = []
    for job in jobs:
        if job["max_salary"] != "":
            max_salaries.append(int(job["max_salary"]))
    return max(max_salaries)


print("max_salary:", get_max_salary("src/jobs.csv"))


def get_min_salary(path):
    jobs = read(path)
    min_salaries = set()
    for job in jobs:
        if job["min_salary"] != "":
            min_salaries.add(int(job["min_salary"]))
    return min(min_salaries)


print("min_salary:", get_min_salary("src/jobs.csv"))


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
