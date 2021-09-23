from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)

    new_JobsList = set()

    for jobs in jobs_list:
        new_JobsList.add(jobs['job_type'])

    return new_JobsList


if __name__ == "__main__":
    get_unique_job_types("src/jobs.csv")


def filter_by_job_type(jobs, job_type):
    job_type_list = []

    for job in jobs:
        if job['job_type'] == job_type:
            job_type_list.append(job)
    return job_type_list


def get_unique_industries(path):
    industries_list = read(path)

    new_industries = set()

    for industry in industries_list:
        if industry['industry'] != '':
            new_industries.add(industry['industry'])

    return new_industries


def filter_by_industry(jobs, industry):

    jobs_by_industry_list = []

    for job in jobs:
        if job['industry'] == industry:
            jobs_by_industry_list.append(job)
    return jobs_by_industry_list


def get_max_salary(path):
    salaries = read(path)
    salary_list = []

    for salary in salaries:
        if salary['max_salary'].isdigit():
            max_salary_to_integer = int(salary['max_salary'])
            salary_list.append(max_salary_to_integer)

    return max(salary_list)


def get_min_salary(path):
    salaries = read(path)
    salary_list = []

    for salary in salaries:
        if salary['min_salary'].isdigit():
            min_salary_to_integer = int(salary['min_salary'])
            salary_list.append(min_salary_to_integer)

    return min(salary_list)


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
