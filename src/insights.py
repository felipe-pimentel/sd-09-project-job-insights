from src.jobs import read
# from jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    unique_jobs = []
    for job in jobs_list:
        if job['job_type'] not in unique_jobs:
            unique_jobs.append(job['job_type'])
    return unique_jobs
    # unique_jobs = []
    # unique_job_type = {}
    # for job in jobs_list:
    #     if job['job_type'] not in unique_job_type:
    #         # unique_jobs.append(job)
    #         unique_job_type[job['job_type']] = {'jobs': 0}
    #     unique_job_type[job['job_type']]['jobs'] += 1
    # print(unique_job_type)
    # return unique_job_type


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
    return []


def get_unique_industries(path):
    jobs_list = read(path)
    unique_industries = []
    for job in jobs_list:
        if job['industry'] not in unique_industries and job['industry'] != '':
            unique_industries.append(job['industry'])
    print(unique_industries)
    return unique_industries


# get_unique_industries('jobs.csv')


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
    max_salary = 0
    for job in jobs_list:
        valid = job['max_salary'] != '' and job['max_salary'] != 'invalid'
        if valid and int(job['max_salary']) > max_salary:
            print(f"{job['max_salary']} > {max_salary}")
            max_salary = int(job['max_salary'])
    print(max_salary)
    return max_salary


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
