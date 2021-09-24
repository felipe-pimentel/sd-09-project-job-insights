from src.jobs import read


def get_unique_job_types(path):
    jobs_listed = read(path)
    job_types = []
    for job in jobs_listed:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    match_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            match_jobs.append(job)
    return match_jobs


def get_unique_industries(path):
    jobs_listed = read(path)
    job_ind = []
    for job in jobs_listed:
        if job["industry"] != "":
            if job["industry"] not in job_ind:
                job_ind.append(job["industry"])
    return job_ind


def filter_by_industry(jobs, industry):
    match_jobs = []
    for job in jobs:
        if job["industry"] == industry:
            match_jobs.append(job)
    return match_jobs


def get_max_salary(path):
    jobs_list = read(path)
    max_salary = []
    for job in jobs_list:
        if job["max_salary"].isnumeric():
            max_salary.append(int(job["max_salary"]))
    set(max_salary)
    print(int(max(max_salary)))
    return max(max_salary)


def get_min_salary(path):
    jobs_list = read(path)
    min_salary = []
    for job in jobs_list:
        if job["min_salary"].isnumeric():
            min_salary.append(int(job["min_salary"]))
    set(min_salary)
    return min(min_salary)


def matches_salary_range(job, salary):
    try:
        if (int(job["max_salary"]) < int(job["min_salary"])):
            raise ValueError()
        return int(job["min_salary"]) <= salary <= int(job["max_salary"])
    except Exception:
        raise ValueError()


def filter_by_salary_range(jobs, salary):
    list_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_jobs.append(job)
        except Exception:
            pass
    return list_jobs
