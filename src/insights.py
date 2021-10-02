import src.jobs


def get_unique_job_types(path):
    jobs_list = src.jobs.read(path)
    data_jobs_types = set()
    for job in jobs_list:
        for type in job["job_type"].split(","):
            data_jobs_types.add(type)
    return data_jobs_types


def filter_by_job_type(jobs, job_type):
    filter_job_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            filter_job_type.append(job)
    return filter_job_type


def get_unique_industries(path):
    jobs_list = src.jobs.read(path)
    data_jobs_industries = set()
    for job in jobs_list:
        if job["industry"] != "":
            data_jobs_industries.add(job["industry"])
    return data_jobs_industries


def filter_by_industry(jobs, industry):
    filter_industry = []
    for job in jobs:
        if job["industry"] == industry:
            filter_industry.append(job)
    return filter_industry


def get_max_salary(path):
    jobs_list = src.jobs.read(path)
    data_jobs_max_salary = set()
    for job in jobs_list:
        try:
            if job["max_salary"] != "":
                data_jobs_max_salary.add(int(job["max_salary"]))
        except ValueError:
            print('Campo não encontrado')
    return max(data_jobs_max_salary)


def get_min_salary(path):
    jobs_list = src.jobs.read(path)
    data_jobs_min_salary = set()
    for job in jobs_list:
        try:
            if job["min_salary"] != "":
                data_jobs_min_salary.add(int(job["min_salary"]))
        except ValueError:
            print('Campo não encontrado')
    return min(data_jobs_min_salary)


def matches_salary_range(job, salary):
    try:
        if job['min_salary'] <= salary <= job['max_salary']:
            return True
        elif job['min_salary'] > job['max_salary']:
            raise ValueError
        else:
            return False
    except (TypeError, ValueError, KeyError):
        raise ValueError


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
