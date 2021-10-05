from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)

    types_list = set()

    for job in jobs_list:
        types_list.add(job["job_type"])

    return types_list


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []

    for job in jobs:
        if (job["job_type"] == job_type):
            filtered_jobs.append(job)

    return filtered_jobs


def get_unique_industries(path):
    jobs_list = read(path)

    industries_list = set()

    for job in jobs_list:
        if (job["industry"] != ""):
            industries_list.add(job["industry"])

    return industries_list


def filter_by_industry(jobs, industry):
    filtered_jobs = []

    for job in jobs:
        if (job["industry"] == industry):
            filtered_jobs.append(job)

    return filtered_jobs


def get_max_salary(path):
    jobs_list = read(path)

    salary_list = set()

    for job in jobs_list:

        job_max_salary = job["max_salary"]

        if (job_max_salary.isnumeric()):
            salary_list.add(int(job_max_salary))

    max_salary = max(salary_list, key=int)

    return max_salary


def get_min_salary(path):
    jobs_list = read(path)

    salary_list = set()

    for job in jobs_list:

        job_min_salary = job["min_salary"]

        if (job_min_salary.isnumeric()):
            salary_list.add(int(job_min_salary))

    min_salary = min(salary_list, key=int)

    return min_salary


def matches_salary_range(job, salary):
    if not (
        isinstance(job.get("min_salary"), int)
        or isinstance(job.get("max_salary"), int)
    ):
        raise ValueError("min_salary and max_salary must be an integer")

    if not isinstance(salary, int):
        raise ValueError("salary must be an integer")

    if ("min_salary" not in job or "max_salary" not in job):
        raise ValueError("min_salary and max_salary must exists")

    if (job["min_salary"] > job["max_salary"]):
        raise ValueError("max_salary must be bigger than min_salary")

    return int(job["min_salary"]) <= salary <= int(job["max_salary"])


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
