import src.jobs


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
            pass
    print(result)
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
            pass
    return min(result)


def matches_salary_range(job, salary):
    try:
        if int(job['min_salary'] > job['max_salary']):
            raise ValueError
        elif int(job['min_salary']) <= int(salary) <= int(job['max_salary']):
            return True
        else:
            return False
    except (TypeError, ValueError, KeyError):
        raise ValueError


def filter_by_salary_range(jobs, salary):
    by_salary_list = []

    for i in jobs:
        try:
            if matches_salary_range(i, salary):
                by_salary_list.append(i)
        except ValueError:
            pass
    return by_salary_list
