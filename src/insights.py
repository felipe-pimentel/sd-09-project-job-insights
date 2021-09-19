from .jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)

    jobs_types = set()

    for job in jobs_list:
        jobs_types.add(job["job_type"])

    return jobs_types


def filter_by_job_type(jobs, job_type):

    select_jobs = []

    for job in jobs:
        if (job["job_type"] == job_type):
            select_jobs.append(job)

    return select_jobs


def get_unique_industries(path):
    jobs_list = read(path)

    jobs_industries = set()

    for job in jobs_list:
        if (job["industry"] != ""):
            jobs_industries.add(job["industry"])

    return jobs_industries


def filter_by_industry(jobs, industry):
    select_industries = []

    if (industry != ""):
        for job in jobs:
            if (job["industry"] == industry):
                select_industries.append(job)

    return select_industries


def get_max_salary(path):
    jobs_list = read(path)

    max_salary = set()

    for job in jobs_list:
        if ("max_salary" in job):
            if (job["max_salary"].isdigit()):
                max_salary.add(int(job["max_salary"]))

    return max(max_salary)


def get_min_salary(path):
    jobs_list = read(path)

    min_salary = set()

    for job in jobs_list:
        if ("min_salary" in job):
            if (job["min_salary"].isdigit()):
                min_salary.add(int(job["min_salary"]))

    return min(min_salary)


def salaries_range_validation(job):
    if ("min_salary" not in job or "max_salary" not in job):
        raise ValueError()

    if (not isinstance(job["min_salary"], int)):
        raise ValueError()

    if (not isinstance(job["max_salary"], int)):
        raise ValueError()

    if (job["min_salary"] > job["max_salary"]):
        raise ValueError()


def salary_validation(salary):
    if (not isinstance(salary, int)):
        raise ValueError()


def matches_salary_range(job, salary):
    salaries_range_validation(job)
    salary_validation(salary)

    if (salary >= job["min_salary"] and salary <= job["max_salary"]):
        return True

    return False


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
