from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    jobs = []
    for job in data:
        if job["job_type"] in jobs:
            continue
        if job["job_type"] == "":
            continue

        jobs.append(job["job_type"])

    return jobs


def filter_by_job_type(jobs, job_type):
    data = []

    for job in jobs:
        if job["job_type"] == job_type:
            data.append(job)

    return data


def get_unique_industries(path):
    data = read(path)
    industries = []

    for obj in data:
        if obj["industry"] == "":
            continue

        if not obj["industry"] in industries:
            industries.append(obj["industry"])

    return industries


def filter_by_industry(jobs, industry):
    job_filter = []

    for obj in jobs:
        if obj["industry"] == industry:
            job_filter.append(obj)

    return job_filter


def get_max_salary(path):
    data = read(path)
    highestSalary = 0

    for obj in data:
        value = obj["max_salary"]

        if value == "":
            continue
        if value.isdigit():
            if int(value) > highestSalary:
                highestSalary = int(value)

    return highestSalary


def get_min_salary(path):
    data = read(path)
    min_salary = 999999999
    for s in data:
        if s["min_salary"].isdigit():
            if int(s["min_salary"]) < min_salary:
                min_salary = int(s["min_salary"])
    return int(min_salary)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError(
            "`job['min_salary']` or `job['max_salary']` doesn't exists"
        )
    elif (type(job["min_salary"]) is not int) or (
        type(job["max_salary"]) is not int
    ):
        raise ValueError(
            "`job['min_salary']` or `job['max_salary']` aren't valid integers"
        )
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError(
            "job['`min_salary']` is greather than `job['max_salary']`"
        )
    elif type(salary) is not int:
        raise ValueError("salary` isn't a valid integer")
    else:
        return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    salary_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salary_list.append(job)
        except ValueError:
            pass
    return salary_list
