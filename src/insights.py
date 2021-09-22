from src.jobs import read


def get_unique_job_types(path):
    job_types = set()
    jobs = read(path)

    for job in jobs:
        job_types.add(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):

    jobs_filtered = []

    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filtered.append(job)

    return jobs_filtered


def get_unique_industries(path):

    industri_types = set()
    jobs = read(path)
    for job in jobs:
        if job["industry"] != "":
            industri_types.add(job["industry"])

    return industri_types


def filter_by_industry(jobs, industry):
    jobs_filtered = [job for job in jobs if job["industry"] == industry]

    return jobs_filtered


def get_max_salary(path):
    jobs = read(path)

    max_sal = 0

    for job in jobs:
        if job["max_salary"].isnumeric() and int(job["max_salary"]) > max_sal:
            max_sal = int(job["max_salary"])

    return max_sal


def get_min_salary(path):
    jobs = read(path)

    min_salary = []

    for job in jobs:
        if job["min_salary"].isnumeric():
            min_salary.append(int(job["min_salary"]))

    min_salary.sort()

    return min_salary[0]


def matches_salary_range(job, salary):
    if not (
        "min_salary" in job.keys()
        and "max_salary" in job.keys()
        and isinstance(job["min_salary"], int)
        and isinstance(job["max_salary"], int)
        and job["min_salary"] < job["max_salary"]
    ):
        raise ValueError("Verifique min_salary e max_salary")

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
