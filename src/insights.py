from src.jobs import read


def get_unique_job_types(path):
    returned_jobs = read(path)
    job_types = []
    for job in returned_jobs:
        if job["job_type"] != "":
            job_types.append(job["job_type"])
    job_types = list(dict.fromkeys(job_types))
    return job_types


def filter_by_job_type(jobs, job_type):
    found_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            found_jobs.append(job)
    return found_jobs


def get_unique_industries(path):
    returned_jobs = read(path)
    industries = []
    for job in returned_jobs:
        if job["industry"] != "":
            industries.append(job["industry"])
    industries = list(dict.fromkeys(industries))
    return industries


def filter_by_industry(jobs, industry):
    found_industries = []
    for job in jobs:
        if job["industry"] == industry:
            found_industries.append(job)
    return found_industries


def get_max_salary(path):
    returned_jobs = read(path)
    salaries = []
    for job in returned_jobs:
        try:
            if job["max_salary"] != "":
                salaries.append(int(job["max_salary"]))
        except ValueError:
            print("Valor não convertido")
    return max(salaries)


def get_min_salary(path):
    returned_jobs = read(path)
    salaries = []
    for job in returned_jobs:
        try:
            if job["min_salary"] != "":
                salaries.append(int(job["min_salary"]))
        except ValueError:
            print("Valor não convertido")
    return min(salaries)


def check_if_keys_exists(job):
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError


def check_if_values_are_int(job, salary):
    if not isinstance(salary, int):
        raise ValueError
    if not isinstance(job["max_salary"], int):
        raise ValueError
    if not isinstance(job["min_salary"], int):
        raise ValueError


def matches_salary_range(job, salary):
    check_if_keys_exists(job)
    check_if_values_are_int(job, salary)
    if job["min_salary"] > job["max_salary"]:
        raise ValueError
    elif salary <= job["max_salary"] and salary >= job["min_salary"]:
        return True
    else:
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
