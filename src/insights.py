import csv


def get_unique_job_types(path):

    with open(path) as file:
        jobs_reader = csv.DictReader(file)
        jobs = [job for job in jobs_reader]

    job_types = []

    for job in jobs:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    job_upper = job_type.upper()
    jobs_type = []

    for job in jobs:
        print(job["job_type"])
        if job["job_type"] == job_upper:
            jobs_type.append(job)

    return jobs_type


def get_unique_industries(path):
    with open(path) as file:
        jobs_reader = csv.DictReader(file)
        jobs = [job for job in jobs_reader]

        industries = []

        for job in jobs:
            if job["industry"] not in industries and job["industry"] != "":
                industries.append(job["industry"])

    return industries


def filter_by_industry(jobs, industry):
    jobs_type = []

    for job in jobs:
        print(job["industry"])
        if job["industry"] == industry:
            jobs_type.append(job)

    return jobs_type


def get_max_salary(path):

    with open(path) as file:
        jobs_reader = csv.DictReader(file)
        jobs = [job for job in jobs_reader]

        # max_salary = jobs.index(jobs)
        industries = []

        for job in jobs:
            if job["job_title"] != "" and job["job_title"] not in industries:
                # print(len(job["job_title"]))
                # print({job["job_title"]: job["max_salary"]})
                industries.append({job["job_title"]: job["max_salary"]})
    # print(industries)
    # return industries
    # pass


# get_max_salary("jobs.csv")


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    pass


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


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
