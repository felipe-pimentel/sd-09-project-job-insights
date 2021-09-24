from src.jobs import read


def get_unique_job_types(path):
    csv_file = read(path)
    job_types = set()

    for row in csv_file:
        job_types.add(row["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    return []


def get_unique_industries(path):
    csv_file = read(path)
    unique_industries = set()

    for row in csv_file:
        industry = row["industry"]
        if industry != "":
            unique_industries.add(industry)
    return unique_industries


def filter_by_industry(jobs, industry):
    return []


def get_max_salary(path):
    csv_file = read(path)
    maximus_salaries = set()

    for row in csv_file:
        max_salary = row["max_salary"]
        if max_salary.isdigit():
            maximus_salaries.add(int(max_salary))

    highest_salary = max(maximus_salaries, key=int)
    return highest_salary


def get_min_salary(path):
    csv_file = read(path)
    minimum_salaries = set()

    for row in csv_file:
        min_salary = row["min_salary"]
        if min_salary.isdigit():
            minimum_salaries.add(int(min_salary))
    lowest_salary = min(minimum_salaries, key=int)
    return lowest_salary


def matches_salary_range(job, salary):
    pass


def filter_by_salary_range(jobs, salary):
    return []
