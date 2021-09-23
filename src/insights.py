from src.jobs import read


def get_unique_job_types(path):
    job_type = set()
    list_categories = read(path)
    for jobs in list_categories:
        job_type.add(jobs["job_type"])
    return job_type


def filter_by_job_type(jobs, job_type):

    list_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            list_jobs.append(job)
    return list_jobs


def get_unique_industries(path):
    industry_type = set()
    for industry in read(path):
        if len(industry["industry"]) != 0:
            industry_type.add(industry["industry"])
    return industry_type


def filter_by_industry(jobs, industry):
    jobs_in_industry = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_in_industry.append(job)
    return jobs_in_industry


def get_max_salary(path):
    jobs = read(path)

    max_salary = []

    for job in jobs:
        try:
            max_salary.append(int(job["max_salary"]))
        except ValueError:
            pass
    max_salary.sort()
    return max_salary[-1]


def get_min_salary(path):
    jobs = read(path)

    min_salary = []

    for job in jobs:
        try:
            min_salary.append(int(job["min_salary"]))
        except ValueError:
            pass
    min_salary.sort()
    return min_salary[0]


def matches_salary_range(job, salary):
    for value in job:
        try:
            value["max_salary"] < salary > value["min_salary"]
            return True
        except ValueError:
            return False


def filter_by_salary_range(jobs, salary):
    return []
