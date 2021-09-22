from src.jobs import read


def get_unique_job_types(path):
    jobs_data = read(path)

    jobs_list = []
    for job in jobs_data:
        jobs_list.append(job["job_type"])

    jobs_list = list(dict.fromkeys(jobs_list))
    return jobs_list


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    industries_data = read(path)

    industries_list = []
    for industry in industries_data:
        if len(industry["industry"]) > 0:
            industries_list.append(industry["industry"])

    industries_list = list(dict.fromkeys(industries_list))
    return industries_list


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    jobs = read(path)
    max_salary_list = []
    for job in jobs:
        if job["max_salary"].isnumeric():
            max_salary_list.append(int(job["max_salary"]))
    return max(max_salary_list)


def get_min_salary(path):
    jobs = read(path)
    min_salary_list = []
    for job in jobs:
        if job["min_salary"].isnumeric():
            min_salary_list.append(int(job["min_salary"]))
    return min(min_salary_list)


def isInt(number):
    if type(number) is int:
        return True
    return False


def matches_salary_range(job, salary):
    if not ("min_salary" in job and "max_salary" in job):
        raise ValueError()
    if not (isInt(job["min_salary"]) or isInt(job["max_salary"])):
        raise ValueError()
    if (job["min_salary"] > job["max_salary"]):
        raise ValueError()
    if not isInt(salary):
        raise ValueError()
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    # para utilizar a função acima é preciso o try catch
    # (pois a função "matches_salary_range") trata exceções
    by_salary_list = []

    for i in jobs:
        try:
            if matches_salary_range(i, salary):
                by_salary_list.append(i)
        except ValueError:
            pass
    return by_salary_list
