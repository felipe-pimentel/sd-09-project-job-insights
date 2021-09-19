from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    job_types = set()
    for job in data:
        job_types.add(job["job_type"])
    return [*job_types]


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    data = read(path)
    industries = set()
    for job in data:
        industries.add(job["industry"])
    return [line for line in industries if line != ""]


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    data = read(path)
    all_salaries = set()
    for job in data:
        if job["max_salary"] != "" and job["max_salary"].isdigit():
            all_salaries.add(int(job["max_salary"]))
    return max(all_salaries)


def get_min_salary(path):
    data = read(path)
    all_salaries = set()
    for job in data:
        if job["min_salary"] != "" and job["min_salary"].isdigit():
            all_salaries.add(int(job["min_salary"]))
    return min(all_salaries)


def matches_salary_range(job, salary):
    keys = ["min_salary", "max_salary"]
    if not all(key in job for key in keys):
        raise ValueError("Missing key")
    if (
        type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
    ):
        raise ValueError("Invalid type")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("Min salary is bigger than max salary")
    if type(salary) is not int:
        raise ValueError("Invalid salary type")
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    matched_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                matched_jobs.append(job)
        except ValueError:
            # print(message)
            pass
    return matched_jobs
