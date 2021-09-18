from src.jobs import read

# from jobs import read
# import json

path = "src/jobs.csv"


def get_unique_job_types(path):
    job_types = set()
    full_list = read(path)
    for job in full_list:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    # jobs é um dic com lista de jobs
    # job_type é uma string
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    industry_types = set()
    full_list = read(path)
    for job in full_list:
        industry_type = job["industry"]
        if industry_type != "":
            industry_types.add(industry_type)
    return industry_types


def filter_by_industry(jobs, industry):
    # jobs é um dic com lista de jobs
    # industry é uma string
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    full_list = read(path)
    salary_list = []
    for job in full_list:
        if job["max_salary"].isnumeric():
            salary_list.append(int(job["max_salary"]))
    salary_list.sort()
    return salary_list[-1]


def get_min_salary(path):
    full_list = read(path)
    salary_list = []
    for job in full_list:
        if job["min_salary"].isnumeric():
            salary_list.append(int(job["min_salary"]))
    salary_list.sort()
    return salary_list[0]


def matches_salary_range(job, salary):
    # jobs é um dict com min e max salary
    # erro quando min ou max está ausente
    # erro quando min ou max não tem valor numerico
    # jobs é um int
    if not (
        "min_salary" in job.keys()
        and isinstance(job["min_salary"], int)
        and job["min_salary"] >= 0
    ):
        raise ValueError("Problemas com o min_salary")
    if not (
        "max_salary" in job.keys()
        and isinstance(job["max_salary"], int)
        and job["max_salary"] >= 0
    ):
        raise ValueError("Problemas com o max_salary")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("O min é maior que o max")
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    job_list = []
    for job in jobs:
        if (
            ("min_salary" in job.keys() and "max_salary" in job.keys())
            and (job["min_salary"] is not None and job['min_salary' != ''])
            and (job["max_salary"] is not None and job['max_salary' != ''])
            and job["min_salary"] <= job["max_salary"]
            and matches_salary_range(job, salary)
        ):
            print(job)
            job_list.append(job)
    return job_list
