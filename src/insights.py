from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    job_types = read(path)

    key_unique = set()

    for row in job_types:
        key_unique.add(row['job_type'])

    return key_unique


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
    # tive auxilio do aluno joão 
    # https://github.com/Galaraz
    filter = []
   
    for jobItem in jobs:
        if jobItem['job_type'] == job_type:
            filter.append(jobItem)

    return filter


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    industries_types = read(path)

    industries_unique = set()

    for row in industries_types:
        if row["industry"] != '':
            industries_unique.add(row['industry'])

    return industries_unique


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
    filter = []

    for jobItem in jobs:
        if(jobItem['industry']) == industry:
            filter.append(jobItem)

    return filter


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    salary = read(path)

    maximum_salary = []

    for row in salary:
        if row['max_salary'] != '' and row['max_salary'].isdigit():

            maximum_salary.append(int(row['max_salary']))    
    
    return max(maximum_salary)


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
    salary = read(path)

    minimun_salary = []

    for row in salary:
        if row['min_salary'] != '' and row['min_salary'].isdigit():

            minimun_salary.append(int(row['min_salary']))    
    
    return min(minimun_salary)


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
    if ("min_salary" or "max_salary") not in job:
        raise ValueError("A sua busca não foi encontrada")
    elif type(job["min_salary"] or job["max_salary"] or salary) != int:
        raise ValueError("A sua busca não foi encontrada")
    elif (job["min_salary"] > job["max_salary"]):
        raise ValueError("A sua busca não foi encontrada")
    elif (job["min_salary"] <= salary <= job["max_salary"]):
        return True

    return False


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
    filtSalary = []
    for job in jobs:
        try:
            if (matches_salary_range(job, salary)):
                filtSalary.append(job)
        except Exception:
            print("Inputs error")
    return filtSalary