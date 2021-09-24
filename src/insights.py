from src.jobs import read
# from jobs import read


def get_unique_job_types(path):
    job_types = read(path)

    jobs_unique = set()

    for row in job_types:
        jobs_unique.add(row["job_type"])

    return jobs_unique


# print(get_unique_job_types("src/jobs.csv"))


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
    job_industries = read(path)

    industries_unique = set()

    for row in job_industries:
        if row["industry"] != '':
            industries_unique.add(row["industry"])

    return industries_unique


# print(get_unique_industries('src/jobs.csv'))


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
    job_max_salary = read(path)

    salary_max = []

    for row in job_max_salary:
        if row["max_salary"] != '' and row["max_salary"].isdigit():
            salary_max.append(int(row["max_salary"]))
            # try:
            #     if salary_max < int(row["max_salary"]):
            #         salary_max = int(row["max_salary"])
            # except ValueError:
            #     print("Não deu certo. Tente outra vez!")

    return max(salary_max)


# print(get_max_salary("src/jobs.csv"))


def get_min_salary(path):
    job_min_salary = read(path)

    salary_min = []

    for row in job_min_salary:
        if row["min_salary"] != '' and row["min_salary"].isdigit():
            salary_min.append(int(row["min_salary"]))

    return min(salary_min)


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
