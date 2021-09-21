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
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    # return []
    pass


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
