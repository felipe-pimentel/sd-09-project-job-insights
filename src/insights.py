from src.jobs import read


def get_unique_job_types(path):
    csv_list = read(path)
    csv_type_list = set()
    for job in csv_list:
        csv_type_list.add(job["job_type"])
    return csv_type_list


def filter_by_job_type(jobs, job_type):
    job_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_list.append(job)
    return job_list


def get_unique_industries(path):
    job_list = read(path)
    industries = set()
    for industry in job_list:
        if industry["industry"] != "":
            industries.add(industry["industry"])
    return industries


def filter_by_industry(jobs, industry):
    industry_list = []
    for job in jobs:
        if job["industry"] == industry:
            industry_list.append(job)
    return industry_list


def get_max_salary(path):
    job_list = read(path)
    max_salary = []
    for job in job_list:
        if job["max_salary"].isnumeric():
            max_salary.append(int(job["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    job_list = read(path)
    min_salary = []
    for job in job_list:
        if job["min_salary"].isnumeric():
            min_salary.append(int(job["min_salary"]))
    return min(min_salary)


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
