from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    jobs_type = set()

    for job in jobs:
        jobs_type.add(job["job_type"])
    return jobs_type


def filter_by_job_type(jobs, job_type):
    jobs_selected = []

    for job in jobs:
        if job["job_type"] == job_type:
            jobs_selected.append(job)

    return jobs_selected


def get_unique_industries(path):
    jobs = read(path)
    industries = set()

    for job in jobs:
        if job["industry"] != "":
            industries.add(job["industry"])

    return industries


def filter_by_industry(jobs, industry):
    jobs_selected = []

    for job in jobs:
        if job["industry"] == industry:
            jobs_selected.append(job)

    return jobs_selected


def get_max_salary(path):
    salaries = []
    jobs = read(path)

    for job in jobs:
        if job["max_salary"] != "" and job["max_salary"] != "invalid":
            salaries.append(int(job["max_salary"]))

    return max(salaries)


def get_min_salary(path):
    salaries = []
    jobs = read(path)

    for job in jobs:
        if job["min_salary"] != "" and job["min_salary"] != "invalid":
            salaries.append(int(job["min_salary"]))

    return min(salaries)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Algum range máximo e mínimo de salario está vazio")

    if (
        type(job["max_salary"]) is not int
        or type(job["min_salary"]) is not int
        or type(salary) is not int
    ):
        raise ValueError("O máximo, mínimo salário ou o salário está vazio")

    if job["max_salary"] - job["min_salary"] < 0:
        raise ValueError("Salário máximo é menor que o salário")

    return job["max_salary"] >= salary >= job["min_salary"]


def filter_by_salary_range(jobs, salary):
    jobs_selected = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary) is True:
                jobs_selected.append(job)
        except ValueError:
            pass

    return jobs_selected
