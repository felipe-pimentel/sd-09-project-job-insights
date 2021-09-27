from src.jobs import read
import sys


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
    jobList = read(path)
    jobTypes = set()
    for job in jobList:
        jobTypes.add(job["job_type"])
    return jobTypes


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
    filteredJobs = []
    for job in jobs:
        if(job["job_type"] == job_type):
            filteredJobs.append(job)
    return filteredJobs


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
    jobList = read(path)
    industryTypes = set()
    for job in jobList:
        if (job["industry"]):
            industryTypes.add(job["industry"])
    return industryTypes


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
    filteredJobs = []
    for job in jobs:
        if(job["industry"] == industry):
            filteredJobs.append(job)
    return filteredJobs


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
    jobList = read(path)
    maxSalary = 0
    for job in jobList:
        if (job["max_salary"] and job["max_salary"] != "invalid"):
            if(int(job["max_salary"]) > maxSalary):
                maxSalary = int(job["max_salary"])
    return maxSalary


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
    jobList = read(path)
    minSalary = sys.maxsize
    for job in jobList:
        if (job["min_salary"] and job["min_salary"] != "invalid"):
            if(int(job["min_salary"]) < minSalary):
                minSalary = int(job["min_salary"])
    return minSalary


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

    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or job["min_salary"] > job["max_salary"]
        or type(salary) != int
    ):
        raise ValueError("Deu ruim")
    return (job["min_salary"] <= salary <= job["max_salary"])


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
    filteredJobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filteredJobs.append(job)
        except ValueError:
            pass
    return filteredJobs
