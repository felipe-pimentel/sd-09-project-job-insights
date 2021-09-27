from src.jobs import read


def get_unique_job_types(path):
    all_jobs = read(path)
    job_types = []
    for job in all_jobs:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    all_jobs_by_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            all_jobs_by_type.append(job)
    return all_jobs_by_type


def get_unique_industries(path):
    all_industries = read(path)
    industries_types = []
    for row in all_industries:
        industry = row["industry"]
        if industry not in industries_types and len(industry) > 0:
            industries_types.append(industry)
    return industries_types


def filter_by_industry(jobs, industry):
    all_jobs_by_industry = []
    for job in jobs:
        if job["industry"] == industry:
            all_jobs_by_industry.append(job)
    return all_jobs_by_industry


def get_max_salary(path):
    all_salary = read(path)
    max_salary = 0
    for row in all_salary:
        salary = row["max_salary"]
        if salary.isdigit() and max_salary < int(salary):
            max_salary = int(salary)
    return max_salary


def get_min_salary(path):
    all_salary = read(path)
    min_salary = []
    for row in all_salary:
        salary = row["min_salary"]
        if salary.isdigit():
            min_salary.append(int(salary))
    return min(min_salary)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("invalid entries")
    elif type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError("invalid entries")
    elif type(salary) != int:
        raise ValueError("invalid entries")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("invalid entries")
    return (job["min_salary"] <= salary < job["max_salary"])


def filter_by_salary_range(jobs, salary):
    jobs_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_list.append(job)
        except ValueError:
            pass
    print(jobs_list)
    return jobs_list
