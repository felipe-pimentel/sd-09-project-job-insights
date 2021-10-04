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
    all_jobs_list = read(path)

    jobs_type = set()
    for job_type in all_jobs_list:
        jobs_type.add(job_type["job_type"])

    return jobs_type


# print(get_unique_job_types("tests/mocks/jobs_with_types.csv"))


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
        if (job["job_type"] == job_type):
            result.append(job)

    return result


# filter_by_job_type(read("tests/mocks/jobs.csv"), "full time")


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
    all_industries_list = read(path)

    industries_type = set()
    for industry_type in all_industries_list:
        if industry_type["industry"] != "":
            industries_type.add(industry_type["industry"])

    return industries_type


# print(get_unique_industries("src/jobs.csv"))


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
        if job["industry"] == industry:
            result.append(job)

    return result


# print(filter_by_industry(
#     jobs.read("tests/mocks/jobs_with_industries.csv"),
#     "solar energy")
# )


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
    all_jobs_list = read(path)

    salary_list = []
    for job in all_jobs_list:
        if job["max_salary"].isdigit():
            salary_list.append(int(job["max_salary"]))

    return max(salary_list)


# print(get_max_salary("src/jobs.csv"))


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
    all_jobs_list = read(path)

    salary_list = []
    for job in all_jobs_list:
        if job["min_salary"].isdigit():
            salary_list.append(int(job["min_salary"]))

    return min(salary_list)


# print(get_min_salary("src/jobs.csv"))


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
    # if "min_salary" not in job or "max_salary" not in job:
    #     raise ValueError

    # if not "min_salary".isnumeric() or not "max_salary".isnumeric():
    #     raise ValueError

    # if int(job["max_salary"]) < 1 or int(job["min_salary"]) < 1:
    #     raise ValueError

    # if int(job["max_salary"]) <= int(job["min_salary"]):
    #     raise ValueError

    # return (int(salary) >= int(job["min_salary"])
    #         and int(salary) <= int(job["max_salary"]))

    try:
        if int(job["max_salary"]) <= int(job["min_salary"]):
            raise ValueError
        else:
            return (int(salary) >= int(job["min_salary"]) and
                    int(salary) <= int(job["max_salary"]))
    except (TypeError, KeyError, ValueError):
        raise ValueError


# job = {"max_salary": 1000, "min_salary": 100}
# print(matches_salary_range(job, 500))


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
    result = []

    return result


# print(filter_by_salary_range(
#     read("tests/mocks/jobs_with_salaries.csv"),
#     2000)
# )
