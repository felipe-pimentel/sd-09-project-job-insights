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
    if not ("min_salary" in job and "max_salary" in job):
        raise ValueError()
    if not (type(job["min_salary"]) is int or type(job["max_salary"]) is int):
        raise ValueError()
    if job["max_salary"] < job["min_salary"]:
        raise ValueError()
    if not type(salary) is int:
        raise ValueError()
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    job_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                job_list.append(job)
        except ValueError:
            pass
    return job_list
