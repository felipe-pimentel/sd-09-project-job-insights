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
    return []


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
