import src.jobs


"""https://towardsdatascience.com/
how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c"""


def get_unique_job_types(path):
    jobs_list = src.jobs.read(path)
    result = set()
    for job in jobs_list:
        for type in job["job_type"].split(","):
            result.add(type)
    return result


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    result = []
    for job in jobs:
        try:
            if job["job_type"] == job_type:
                result.append(job)
        except TypeError:
            # print("Campo inválido")
            pass
    return result


def get_unique_industries(path):
    jobs_list = src.jobs.read(path)
    result = set()
    for job in jobs_list:
        try:
            if job["industry"] != "":
                result.add(job["industry"])
        except ValueError:
            # print("Campo inválido")
            pass
    return result


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
    result = []
    for job in jobs:
        try:
            if job["industry"] == industry:
                result.append(job)
        except TypeError:
            # print("Campo inválido")
            pass
    return result


def get_max_salary(path):
    jobs_list = src.jobs.read(path)
    result = set()
    for job in jobs_list:
        try:
            if job["max_salary"] != "":
                result.add(int(job["max_salary"]))
        except ValueError:
            # print('Campo inválido')
            pass
    return max(result)


def get_min_salary(path):
    jobs_list = src.jobs.read(path)
    result = set()
    for job in jobs_list:
        try:
            if job["min_salary"] != "":
                result.add(int(job["min_salary"]))
        except ValueError:
            print('Campo inválido')
    return min(result)


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
