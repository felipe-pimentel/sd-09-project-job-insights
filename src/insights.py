import csv


def get_unique_job_types(path):

    with open(path) as file:
        jobs_reader = csv.DictReader(file)
        jobs = [job for job in jobs_reader]

    job_types = []

    for job in jobs:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    job_upper = job_type.upper()
    jobs_type = []

    for job in jobs:
        print(job["job_type"])
        if job["job_type"] == job_upper:
            jobs_type.append(job)

    return jobs_type


def get_unique_industries(path):
    with open(path) as file:
        jobs_reader = csv.DictReader(file)
        jobs = [job for job in jobs_reader]

        industries = []

        for job in jobs:
            if job["industry"] not in industries and job["industry"] != "":
                industries.append(job["industry"])

    return industries


def filter_by_industry(jobs, industry):
    jobs_type = []

    for job in jobs:
        print(job["industry"])
        if job["industry"] == industry:
            jobs_type.append(job)

    return jobs_type


def get_max_salary(path):

    with open(path) as file:
        jobs_reader = csv.DictReader(file)
        jobs = [job for job in jobs_reader]

        max_salary = []

        for job in jobs:
            if job["max_salary"].isnumeric():
                max_salary.append(int((job["max_salary"])))

    return max(max_salary)


def get_min_salary(path):
    with open(path) as file:
        jobs_reader = csv.DictReader(file)
        jobs = [job for job in jobs_reader]

        min_salary = []

        for job in jobs:
            if job["min_salary"].isnumeric():
                min_salary.append(int((job["min_salary"])))

    return min(min_salary)


def matches_salary_range(job, salary):
    # SOURCE: verify if is a integer
    # https://pythonguides.com/python-check-if-the-variable-is-an-integer/

    if not ("min_salary" in job.keys() and "max_salary" in job.keys()):
        raise ValueError("min_salary or max_salary don't exist")
    elif not (isinstance(salary, int)):
        raise ValueError("salary is not a number")
    elif not (
        isinstance(job["min_salary"], int)
        and isinstance(job["max_salary"], int)
    ):
        raise ValueError("min_salary or max_salary is not a number")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary is greater than max_salary")

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):

    jobs_salary = []

    for job in jobs:
        if (
            isinstance(salary, int)
            and int(job["min_salary"]) <= int(job["max_salary"])
            and matches_salary_range(job, salary)
        ):

            jobs_salary.append(job)

    return jobs_salary
