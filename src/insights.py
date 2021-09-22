import csv


def get_unique_job_types(path):
    with open(path) as file:
        content = csv.DictReader(file, delimiter=",", quotechar='"')
        unique_jobs = []
        for job in content:
            if job["job_type"] not in unique_jobs:
                unique_jobs.append(job["job_type"])
    return unique_jobs


def filter_by_job_type(jobs, job_type):
    jobs_filtered = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filtered.append(job)
    return jobs_filtered


def get_unique_industries(path):
    with open(path) as file:
        content = csv.DictReader(file, delimiter=",", quotechar='"')
        unique_industries = []
        for job in content:
            if job["industry"] not in unique_industries:
                if job["industry"] != "":
                    unique_industries.append(job["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    jobs_filtered = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_filtered.append(job)
    return jobs_filtered


def get_max_salary(path):
    with open(path) as file:
        content = csv.DictReader(file)
        # cria um elemento que será iteravel
        salaries = set()
        for job in content:
            # verifica que o valor existe
            if job["max_salary"].isdigit() and job["max_salary"] != "":
                # transforma o valor em numero
                salaries.add(int(job["max_salary"]))
        return max(salaries)


def get_min_salary(path):
    with open(path) as file:
        content = csv.DictReader(file)
        salaries = set()
        for job in content:
            if job["min_salary"].isdigit() and job["min_salary"] != "":
                salaries.add(int(job["min_salary"]))
    return min(salaries)


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
    ):
        raise ValueError("error")
    if (
        type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
    ):
        raise ValueError("error")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("error")
    if type(salary) != int:
        raise ValueError("error")

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    jobs_filtered = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_filtered.append(job)
        except ValueError:
            pass
    return jobs_filtered
