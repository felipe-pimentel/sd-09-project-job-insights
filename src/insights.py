from src.jobs import read
# from jobs import read


def get_unique_job_types(path):
    list_jobs = read(path)
    job_types = set()
    for job in list_jobs:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    jobs_by_type = []
    for job in jobs:
        if job_type == job["job_type"]:
            jobs_by_type.append(job)
    return jobs_by_type


def get_unique_industries(path):
    jobs_list = read(path)
    industries = set()
    for job in jobs_list:
        if job["industry"] != '':
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    industries = []
    for job in jobs:
        if industry == job["industry"]:
            industries.append(job)
    return industries


def get_max_salary(path):
    jobs_list = read(path)
    max_salary = []
    for job in jobs_list:
        if (job["max_salary"] != ''):
            try:
                max_salary.append(int(job["max_salary"]))
            except ValueError:
                print('')

    return int(max(max_salary))


def get_min_salary(path):
    jobs_list = read(path)
    min_salary = []
    for job in jobs_list:
        if (job["min_salary"] != ''):
            try:
                min_salary.append(int(job["min_salary"]))
            except ValueError:
                print('')

    return int(min(min_salary))


def check_type_max_and_min_salary(min_salary, max_salary):
    if (
        not isinstance(min_salary, int)
        or not isinstance(max_salary, int)
    ):
        raise ValueError


def matches_salary_range(job, salary):
    if not isinstance(salary, int):
        raise ValueError
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    check_type_max_and_min_salary(job["min_salary"], job["max_salary"])
    if job["min_salary"] > job["max_salary"]:
        raise ValueError

    return job["min_salary"] <= salary <= job["max_salary"]

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
