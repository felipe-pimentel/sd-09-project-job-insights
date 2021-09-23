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
# def verify_valid_salary(job):

def validade_salary_range(job):
    return int(job["min_salary"]) > int(job["max_salary"])


def matches_salary_range(job, salary):
    try:
        if int(job["min_salary"]) > int(job["max_salary"]):
            raise ValueError
        if int(job["max_salary"]) >= salary >= int(job["min_salary"]):
            return True
        else:
            return False
    except (ValueError, TypeError, KeyError):
        raise ValueError

# print(job['min_salary'], job['max_salary'])
# print(matches_salary_range(job, 125000))
# print(matches_salary_range({"max_salary": -1, "min_salary": 10}, 1000))
# invalid_jobs = [
#         {"max_salary": 0, "min_salary": 10},
#         {"max_salary": 10, "min_salary": 100},
#         {"max_salary": -1, "min_salary": 10},
#     ]
# salaries = [0, 1, 5, 1000, 2000, -1, -2]
# for job in invalid_jobs:
#     for salary in salaries:
#         print(matches_salary_range(job, salary))


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
