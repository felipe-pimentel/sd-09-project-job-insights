from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    type_job = [job["job_type"] for job in jobs_list]  # read de traz pra fente
    return list(set(type_job))


#  print(get_unique_job_types("src/jobs.csv"))


def filter_by_job_type(jobs, job_type):
    jobs_list = [
        job for job in jobs
        if job["job_type"] == job_type
    ]
    return jobs_list


#  print(filter_by_job_type(read("src/jobs.csv"), "FULL_TIME"))


def get_unique_industries(path):
    jobs_list = read(path)
    industry_job = [
        job["industry"] for job in jobs_list if job["industry"] != ""]
    return list(set(industry_job))


#  print(get_unique_industries("src/jobs.csv"))


def filter_by_industry(jobs, industry):
    jobs_list = [
        job for job in jobs
        if job["industry"] == industry
    ]
    return jobs_list


#  print(filter_by_industry(read("src/jobs.csv"), "Business Services"))


def get_max_salary(path):
    jobs_list = read(path)
    max_salary = [
        int(job["max_salary"])
        for job in jobs_list if job["max_salary"].isnumeric()
    ]
    return max(max_salary)


# print(get_max_salary("src/jobs.csv"))


def get_min_salary(path):
    jobs_list = read(path)
    min_salary = [
        int(job["min_salary"])
        for job in jobs_list if job["min_salary"].isnumeric()
    ]
    return min(min_salary)


#  print(get_min_salary("src/jobs.csv"))


def matches_salary_range(job, salary):
    if ("min_salary" not in job or "max_salary" not in job
            or type(job["min_salary"]) != int or type(job["max_salary"]) != int
            or type(salary) != int
            or job["min_salary"] > job["max_salary"]):
        raise ValueError
    return job["min_salary"] <= salary <= job["max_salary"]


#  print(matches_salary_range({"max_salary": 20, "min_salary": 15}, -1))


def filter_by_salary_range(jobs, salary):
    list_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_jobs.append(job)
        except ValueError:
            pass
    return list_jobs


#  print(filter_by_salary_range(read("src/jobs.csv"), 150000))
