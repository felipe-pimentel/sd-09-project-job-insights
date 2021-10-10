from src.jobs import read
import re

SALARY_REGEX = r"^\d+$"


def get_unique_job_types(path):
    jobs_list = read(path)
    job_types = []

    for job in jobs_list:
        job_types.append(job["job_type"])

    # método para remover itens duplicados conforme
    # apresentado no terceiro exemplo em:
    # https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
    return list(set(job_types))


def filter_by_job_type(jobs, job_type):
    filtered_list_by_job_type = []

    for job in jobs:
        if job["job_type"] == job_type:
            filtered_list_by_job_type.append(job)

    return filtered_list_by_job_type


def get_unique_industries(path):
    jobs_list = read(path)
    industries = []

    for job in jobs_list:
        if job["industry"] != "":
            industries.append(job["industry"])

    return list(set(industries))


def filter_by_industry(jobs, industry):
    filtered_list_by_industry = []

    for job in jobs:
        if job["industry"] == industry:
            filtered_list_by_industry.append(job)

    return filtered_list_by_industry


def get_max_salary(path):
    jobs_list = read(path)
    max_salaries = []

    for job in jobs_list:
        # método para testar uma string utilizando
        # expressões regulares conforme visto em
        # https://blog.geekhunter.com.br/python-regex/#Metodo_rematchpadrao_string_flags0
        if bool(re.match(SALARY_REGEX, job["max_salary"])) is True:
            max_salaries.append(int(job["max_salary"]))

    max_salaries.sort()

    return max_salaries[-1]


def get_min_salary(path):
    jobs_list = read(path)
    min_salaries = []

    for job in jobs_list:
        if bool(re.match(SALARY_REGEX, job["min_salary"])) is True:
            min_salaries.append(int(job["min_salary"]))

    min_salaries.sort()

    return min_salaries[0]


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job.keys()
        or "max_salary" not in job.keys()
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or job["min_salary"] > job["max_salary"]
        or type(salary) != int
    ):
        raise ValueError

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    filtered_jobs_by_salary_range = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs_by_salary_range.append(job)
        except ValueError:
            print("Invalid salary range")

    return filtered_jobs_by_salary_range
