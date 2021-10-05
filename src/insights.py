from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    typesJobs = set()
    for job in jobs:
        typesJobs.add(job["job_type"])
    return typesJobs


def filter_by_job_type(jobs, job_type):
    jobsFiltered = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobsFiltered.append(job)
    return jobsFiltered


def get_unique_industries(path):
    jobs = read(path)
    industries = set()
    for job in jobs:
        if job["industry"] != "":
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    industriesFiltered = []
    for job in jobs:
        if job["industry"] == industry:
            industriesFiltered.append(job)
    return industriesFiltered


def get_max_salary(path):
    jobs = read(path)
    maxSalaries = []
    for job in jobs:
        if job["max_salary"].isdigit():
            maxSalaries.append(int(job["max_salary"]))
    return max(maxSalaries)


def get_min_salary(path):
    jobs = read(path)
    minSalaries = []
    for job in jobs:
        if job["min_salary"].isdigit():
            minSalaries.append(int(job["min_salary"]))
    return min(minSalaries)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Keys not found")

    elif (
        type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError("types invalids")

    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("Value min error")

    elif job["min_salary"] <= salary <= job["max_salary"]:
        return True
    return False
 

def filter_by_salary_range(jobs, salary):
    jobsFiltereds = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary) is True:
                jobsFiltereds.append(job)
        except ValueError:
            print("Values invalids")
    return jobsFiltereds
