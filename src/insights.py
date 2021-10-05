from src.jobs import read


def get_unique_job_types(path):
    data_of_all_jobs = read(path)
    jobs_list = []
    for job in data_of_all_jobs:
        if job["job_type"] not in jobs_list:
            jobs_list.append(job["job_type"])
    return jobs_list


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    all_industries_data = read(path)
    industries_list = []
    for industry in all_industries_data:
        if len(industry["industry"]) > 0:
            industries_list.append(industry["industry"])
    industries_list = list(dict.fromkeys(industries_list))
    return industries_list


def filter_by_industry(jobs, industry):
    jobs_list = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_list.append(job)
    return jobs_list


def get_max_salary(path):
    all_jobs_data = read(path)
    max_salary_list = []
    for job in all_jobs_data:
        if job["max_salary"].isdigit():
            max_salary_list.append(int(job["max_salary"]))
    return max(max_salary_list)


def get_min_salary(path):
    all_jobs_data = read(path)
    min_salary_list = []
    for job in all_jobs_data:
        if job["min_salary"].isdigit():
            min_salary_list.append(int(job["min_salary"]))
    return min(min_salary_list)


def isInt(number):
    if type(number) is int:
        return True
    return False


def matches_salary_range(job, salary):
    if not ("min_salary" in job and "max_salary" in job):
        raise ValueError("Ops! Something wrong!")
    if not (isInt(job["min_salary"]) or isInt(job["max_salary"])):
        raise ValueError("Ops! Something wrong!")
    if (job["min_salary"] > job["max_salary"]):
        raise ValueError("Ops! Something wrong!")
    if not isInt(salary):
        raise ValueError("Ops! Something wrong!")
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    salary_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salary_list.append(job)
        except ValueError:
            ("Ops! Something wrong!")
    return salary_list
