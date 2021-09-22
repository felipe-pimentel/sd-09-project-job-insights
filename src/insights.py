from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    job_types = set()
    for job in data:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    return [row for row in jobs if row["job_type"] == job_type]


def get_unique_industries(path):
    data = read(path)
    industry_types = set()
    for industry in data:
        if industry["industry"]:
            industry_types.add(industry["industry"])
    return industry_types


def filter_by_industry(jobs, industry):
    return [row for row in jobs if row["job_type"] == industry]


def get_max_salary(path):
    data = read(path)
    salaries = set()
    for salary in data:
        if salary["max_salary"].isnumeric():
            salaries.add(int(salary["max_salary"]))
    max_salary = sorted(salaries)[-1]
    return max_salary


def get_min_salary(path):
    data = read(path)
    salaries = set()
    for salary in data:
        if salary["min_salary"].isnumeric():
            salaries.add(int(salary["min_salary"]))
    min_salary = sorted(salaries)[0]
    return min_salary


def matches_salary_range(job, salary):
    if not ("min_salary" in job.keys() and "max_salary" in job.keys()):
        raise ValueError("min_salary and max salary must exist")
    if not (
        isinstance(job["min_salary"], int)
        and isinstance(job["max_salary"], int)
    ):
        raise ValueError("min_salary and max_salary must be numeric values")
    if not (isinstance(salary, int)):
        raise ValueError("salary must be numeric values")
    if (job["min_salary"] > job["max_salary"]):
        raise ValueError("max_salary must be bigger than min_salary")
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    filter_by_salary = set()
    if not ("min_salary" in jobs.keys() and "max_salary" in jobs.keys()):
        raise ValueError("min_salary and max salary must exist")
    if not (
        isinstance(jobs["min_salary"], int)
        and isinstance(jobs["max_salary"], int)
    ):
        raise ValueError("min_salary and max_salary must be numeric values")
    if not (isinstance(salary, int)):
        raise ValueError("salary must be numeric values")
    if (jobs["min_salary"] > jobs["max_salary"]):
        raise ValueError("max_salary must be bigger than min_salary")
    pass
