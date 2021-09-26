from src.jobs import read

# from jobs import read


def get_unique_job_types(path):
    jobs_dictionary = read(path)
    job_types = set()
    for job in jobs_dictionary:
        job_types.add(job["job_type"])
    return [*job_types]


def filter_by_job_type(jobs, job_type):
    jobs_list = []

    for job in jobs:
        if job["job_type"] == job_type:
            jobs_list.append(job)

    return jobs_list


def get_unique_industries(path):
    jobs_dictionary = read(path)
    industry_types = set()
    for row in jobs_dictionary:
        if row["industry"] != "":
            industry_types.add(row["industry"])
    return [*industry_types]


def filter_by_industry(jobs, industry):
    jobs_list = []

    for job in jobs:
        if job["industry"] == industry:
            jobs_list.append(job)

    return jobs_list


def get_max_salary(path):
    jobs_dictionary = read(path)
    max_salary = 0
    for row in jobs_dictionary:
        if row["max_salary"] != "" and row["max_salary"].isdigit():
            if int(row["max_salary"]) > max_salary:
                max_salary = int(row["max_salary"])

    return max_salary


def get_min_salary(path):
    jobs_dictionary = read(path)
    min_salary = 100000000
    for row in jobs_dictionary:
        if row["min_salary"] != "" and row["min_salary"].isdigit():
            if 0 < int(row["min_salary"]) < min_salary:
                min_salary = int(row["min_salary"])

    return min_salary


def matches_salary_range(job, salary):
    try:
        job_base = [
            int(job["min_salary"]),
            int(job["max_salary"]),
        ]
        if job_base[0] > job_base[1]:
            raise ValueError(
                "O salário mínimo indicado é maior do que o máximo"
            )
        verify = job_base[0] <= salary <= job_base[1]
        return verify
    except Exception:
        raise ValueError("""Algo deu errado""")


def filter_by_salary_range(jobs, salary):
    jobs_ok = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_ok.append(job)
        except ValueError:
            "Error"
    return jobs_ok
