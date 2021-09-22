from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    job_types = set()
    for job in jobs_list:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    result = []
    for job in jobs:
        if job["job_type"] == job_type:
            result.append(job)
    return result


def get_unique_industries(path):
    jobs_list = read(path)
    industries = set()
    for job in jobs_list:
        if (job["industry"] != ""):
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    result = []
    for job in jobs:
        if job["industry"] == industry:
            result.append(job)
    return result


def get_max_salary(path):
    jobs = read(path)
    max_salaries = []
    for job in jobs:
        if job["max_salary"] != "" and job["max_salary"] != 'invalid':
            max_salaries.append(int(job["max_salary"]))
    return max(max_salaries)


# print("max_salary:", get_max_salary("src/jobs.csv"))
# print("max_salary:", get_max_salary("tests/mocks/jobs_with_salaries.csv"))


def get_min_salary(path):
    jobs = read(path)
    min_salaries = set()
    for job in jobs:
        if job["min_salary"] != "" and job["max_salary"] != 'invalid':
            min_salaries.add(int(job["min_salary"]))
    return min(min_salaries)


# print("min_salary:", get_min_salary("src/jobs.csv"))


def matches_salary_range(job, salary):
    try:
        if int(job["min_salary"]) > int(job["max_salary"]):
            raise ValueError
        elif int(job["max_salary"]) >= salary >= int(job["min_salary"]):
            return True
        else:
            return False
    except (ValueError, TypeError, KeyError):
        raise ValueError


job = read("src/jobs.csv")[100]


def filter_by_salary_range(jobs, salary):
    jobs_with_validy_salary = [
        job for job in jobs
        if job["max_salary"] != '' and job["min_salary"] != '']

    filtered_jobs = []
    for job in jobs_with_validy_salary:
        if matches_salary_range(job, salary) is True:
            filtered_jobs.append(job)
    return filtered_jobs


# filter_by_salary_range(read("src/jobs.csv"), 200000)
