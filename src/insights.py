from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    job_type = set()
    for job in jobs_list:
        job_type.add(job["job_type"])
    return job_type


def filter_by_job_type(jobs, job_type):
    job_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_list.append(job)
    return job_list


def get_unique_industries(path):
    jobs_list = read(path)
    industries = set()
    for job in jobs_list:
        if len(job["industry"]) > 0:
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    job_list = []
    for job in jobs:
        if job["industry"] == industry:
            job_list.append(job)
    return job_list


def get_max_salary(path):
    jobs_list = read(path)
    max_salary_list = []
    for job in jobs_list:
        if job["max_salary"].isnumeric():
            max_salary_list.append(int(job["max_salary"]))
    return max(max_salary_list)


def get_min_salary(path):
    jobs_list = read(path)
    min_salary_list = []
    for job in jobs_list:
        if job["min_salary"].isnumeric():
            min_salary_list.append(int(job["min_salary"]))
    return min(min_salary_list)


def matches_salary_range(job, salary):
    if not ("min_salary" in job and "max_salary" in job):
        raise ValueError()
    if not (type(job["min_salary"]) is int or type(job["max_salary"]) is int):
        raise ValueError()
    if (job["min_salary"] > job["max_salary"]):
        raise ValueError()
    if not type(salary) is int:
        raise ValueError()
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list.append(job)
        except ValueError:
            pass
    return list
