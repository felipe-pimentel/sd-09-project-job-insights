from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    job_types = set()
    for job in jobs:
        if job["job_type"] != "":
            job_types.add(job["job_type"])
    return list(job_types)


def filter_by_job_type(jobs, job_type):
    jobs_by_job_type = list()
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_by_job_type.append(job)
    return jobs_by_job_type


def get_unique_industries(path):
    jobs = read(path)
    industries = set()
    for job in jobs:
        if job["industry"] != "":
            industries.add(job["industry"])
    return list(industries)


def filter_by_industry(jobs, industry):
    jobs_by_industry = list()
    for job in jobs:
        if job["industry"] == industry:
            jobs_by_industry.append(job)
    return jobs_by_industry


def get_max_salary(path):
    jobs = read(path)
    max_salary = set()
    for job in jobs:
        if job["max_salary"].isnumeric():
            max_salary.add(int(job["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    jobs = read(path)
    min_salary = set()
    for job in jobs:
        if job["min_salary"].isnumeric():
            min_salary.add(int(job["min_salary"]))
    return min(min_salary)


def matches_salary_range(job, salary):
    if ("min_salary" not in job or
        "max_salary" not in job or
        type(job["min_salary"]) != int or
        type(job["max_salary"]) != int or
        type(salary) != int or
            job["min_salary"] > job["max_salary"]):
        raise ValueError

    return salary <= job["max_salary"] and salary >= job["min_salary"]


def filter_by_salary_range(jobs, salary):
    jobs_by_salary_range = list()
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_by_salary_range.append(job)
        except ValueError:
            pass
    return jobs_by_salary_range
