from src.jobs import read


def get_unique_job_types(path):
    unique_job_types = list([jobs["job_type"] for jobs in read(path)])
    return set(unique_job_types)


def filter_by_job_type(jobs, job_type):
    jobs_by_type = [job for job in jobs if job["job_type"] == job_type]
    return jobs_by_type


def get_unique_industries(path):
    unique_industries = list(
        [jobs["industry"] for jobs in read(path) if jobs["industry"] != ""]
    )
    return set(unique_industries)


def filter_by_industry(jobs, industry):
    jobs_by_industry = [job for job in jobs if job["industry"] == industry]
    return jobs_by_industry


def int_verify_exceptions(salary):
    try:
        int(salary)
        return True
    except ValueError:
        return False
    except TypeError:
        return False


def get_max_salary(path):
    all_salaries = [
        int(jobs["max_salary"])
        for jobs in read(path)
        if int_verify_exceptions(jobs["max_salary"])
    ]
    return max(all_salaries)


def get_min_salary(path):
    all_salaries = [
        int(jobs["min_salary"])
        for jobs in read(path)
        if int_verify_exceptions(jobs["min_salary"])
    ]
    return min(all_salaries)


def matches_salary_range(job, salary):
    max_value = "max_salary" in job
    min_value = "min_salary" in job

    # https://www.geeksforgeeks.org/check-multiple-conditions-in-if-statement-python/

    if (
        not max_value or not min_value
        or not int_verify_exceptions(job["max_salary"])
        or not int_verify_exceptions(job["min_salary"])
        or job["min_salary"] > job["max_salary"]
        or not int_verify_exceptions(salary)
    ):
        raise ValueError

    salary_verify = job["min_salary"] <= salary <= job["max_salary"]
    return salary_verify


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
