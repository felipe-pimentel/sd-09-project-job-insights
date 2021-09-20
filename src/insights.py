from src import jobs


def get_unique_job_types(path):
    all_jobs = jobs.read(path)
    output = []
    for job in all_jobs:
        if job["job_type"] not in output and job["job_type"] != '':
            output.append(job["job_type"])
    return output


def filter_by_job_type(jobs, job_type):
    output = []
    for job in jobs:
        if job['job_type'] == job_type:
            output.append(job)

    return output


def get_unique_industries(path):
    all_jobs = jobs.read(path)
    output = []
    for job in all_jobs:
        if job["industry"] not in output and job["industry"] != '':
            output.append(job["industry"])
    return output


def filter_by_industry(jobs, industry):
    output = []
    for job in jobs:
        if job['industry'] == industry:
            output.append(job)

    return output


def get_max_salary(path):
    all_jobs = jobs.read(path)
    output = []
    for job in all_jobs:
        if job["max_salary"] not in output and job["max_salary"] != '':
            try:
                output.append(int(job['max_salary']))
            except Exception:
                print("Error in converting")
    return max(output)


def get_min_salary(path):
    all_jobs = jobs.read(path)
    output = []
    for job in all_jobs:
        if job["min_salary"] not in output and job["min_salary"] != '':
            try:
                output.append(int(job['min_salary']))
            except Exception:
                print("Error in converting")
    return min(output)


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
