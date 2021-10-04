from src.jobs import read


def get_unique_job_types(path):
    jobsfile = read(path)
    job_types = set()
    for eachjob in jobsfile:
        job_types.add(eachjob["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    filteredjobs = []
    for eachjob in jobs:
        if (eachjob["job_type"] == job_type):
            filteredjobs.append(eachjob)
    return filteredjobs


def get_unique_industries(path):
    jobsfile = read(path)
    industries = set()
    for eachjob in jobsfile:
        if (eachjob["industry"] != ""):
            industries.add(eachjob["industry"])
    return industries


def filter_by_industry(jobs, industry):
    filteredjobs = []
    for eachjob in jobs:
        if (eachjob["industry"] == industry):
            filteredjobs.append(eachjob)
    return filteredjobs


def get_max_salary(path):
    jobsfile = read(path)
    salaries = set()
    for eachjob in jobsfile:
        if (eachjob["max_salary"].isnumeric()):
            salaries.add(int(eachjob["max_salary"]))
    max_salary = max(salaries, key=int)
    return max_salary


def get_min_salary(path):
    jobsfile = read(path)
    salaries = set()
    for eachjob in jobsfile:
        if (eachjob["min_salary"].isnumeric()):
            salaries.add(int(eachjob["min_salary"]))
    min_salary = min(salaries, key=int)
    return min_salary


def matches_salary_range(job, salary):
    if not (
        isinstance(job.get("min_salary"), int)
        or isinstance(job.get("max_salary"), int)
    ):
        raise ValueError("min e max salary devem ser inteiros")
    if not isinstance(salary, int):
        raise ValueError("salary deve ser inteiro")
    if (
        "min_salary" not in job
        or "max_salary" not in job
    ):
        raise ValueError("min e max salary devem existir")
    if (job["min_salary"] > ["max_salary"]):
        raise ValueError("max salary deve ser maior que min salary")
    check_salary = job["min_salary"] <= salary <= job["max_salary"]
    return check_salary


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
