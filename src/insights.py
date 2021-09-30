from src.jobs import read


def get_unique_job_types(path):
    list_reader = read(path)
    jobs_list = []
    for j in list_reader:
        if j["job_type"] not in jobs_list:
            jobs_list.append(j["job_type"])
    return jobs_list


def filter_by_job_type(jobs, job_type):
    jobs_list = []
    for j in jobs:
        if j["job_type"] == job_type:
            jobs_list.append(j)
    return jobs_list


def get_unique_industries(path):
    list_reader = read(path)
    ind_list = []
    for i in list_reader:
        if i["industry"] not in ind_list and i["industry"] != "":
            ind_list.append(i["industry"])
    return ind_list

def filter_by_industry(jobs, industry):
    job_list = []
    for j in jobs:
        if j["industry"] == industry:
            job_list.append(j)
    return job_list


def get_max_salary(path):
    list_reader = read(path)
    sal_job = []
    max_sal = 0
    for sal in list_reader:
        if sal["max_salary"].isdigit():
            sal_job.append(int(sal["max_salary"]))
    for sal in sal_job:
        if sal > max_sal:
            max_sal = sal
    return max_sal


def get_min_salary(path):
    list_reader = read(path)
    list_sal = []
    min_sal = 100000
    for sal in list_reader:
        if sal["min_salary"].isdigit():
            list_sal.append(int(sal["min_salary"]))
    for sal in list_sal:
        if sal < min_sal:
            min_sal = sal
    return min_sal


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["max_salary"]) is not int
        or type(job["min_salary"]) is not int
        or type(salary) is not int
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError("invalid data")
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    range_sal = []
    for x in jobs:
        try:
            if matches_salary_range(x, salary):
                range_sal.append(x)
        except ValueError:("Error")
    return range_sal
