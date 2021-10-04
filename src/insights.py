from src.jobs import read


def get_unique_job_types(path):
    list_dict = read(path)
    jobs_filter = []
    for job in list_dict:
        if not job["job_type"] in jobs_filter:
            jobs_filter.append(job["job_type"])
    return jobs_filter


def filter_by_job_type(jobs, job_type):
    jobs_filter = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filter.append(job)
    return jobs_filter


def get_unique_industries(path):
    list_dict = read(path)
    ind_filter = []
    for ind in list_dict:
        if not ind["industry"] in ind_filter and ind["industry"] != "":
            ind_filter.append(ind["industry"])
    print(ind_filter)
    return ind_filter


def filter_by_industry(jobs, industry):
    job_filter_by_ind = []
    for job in jobs:
        if job["industry"] == industry:
            job_filter_by_ind.append(job)
    return job_filter_by_ind


def get_max_salary(path):
    list_dict = read(path)
    salary_max = 0
    salary_list = []
    for salary in list_dict:
        if salary["max_salary"].isdigit():
            salary_list.append(int(salary["max_salary"]))

    for salary in salary_list:
        if salary > salary_max:
            salary_max = salary
    return salary_max


def get_min_salary(path):
    list_dict = read(path)
    salary_min = 100000
    salary_list = []
    for salary in list_dict:
        if salary["min_salary"].isdigit():
            salary_list.append(int(salary["min_salary"]))
    for salary in salary_list:
        if salary < salary_min:
            salary_min = salary
    return salary_min


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("not found")

    elif salary is None:
        raise ValueError("not found")

    elif not isinstance(job["min_salary"], int) or not isinstance(
        job["max_salary"], int
    ):
        raise ValueError("not integer")

    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("value does not make sense")

    else:
        return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    filtered_salary_range = []
    for job in jobs:
        if (
            isinstance(salary, int)
            and isinstance(job["min_salary"], int)
            and isinstance(job["max_salary"], int)
        ):
            if job["min_salary"] <= salary <= job["max_salary"]:
                filtered_salary_range.append(job)
    return filtered_salary_range
