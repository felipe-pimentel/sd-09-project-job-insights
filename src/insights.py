from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    types = set()
    for job in jobs_list:
        types.add(job["job_type"])
    return types


def filter_by_job_type(jobs, job_type):
    jobs_by_type = [job for job in jobs if job["job_type"] == job_type]
    return jobs_by_type


def get_unique_industries(path):
    jobs = read(path)
    industries = set()
    for job in jobs:
        if job["industry"]:
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    jobs_by_industry = [job for job in jobs if job["industry"] == industry]
    return jobs_by_industry


def get_max_salary(path):
    jobs = read(path)
    max_salary_list = []
    for job in jobs:
        if job["max_salary"].isdigit():
            max_salary_list.append(int(job["max_salary"]))
    return max(max_salary_list)


def get_min_salary(path):
    jobs = read(path)
    min_salary_list = []
    for job in jobs:
        if job["min_salary"].isdigit():
            min_salary_list.append(int(job["min_salary"]))
    return min(min_salary_list)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Houve um problema")

    elif (
        type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError("Houve um problema")

    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("Houve um problema")

    elif job["min_salary"] <= salary <= job["max_salary"]:
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
