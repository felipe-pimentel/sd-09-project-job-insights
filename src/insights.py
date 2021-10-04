from src.jobs import read


def get_unique_job_types(path):
    general_list = read(path)

    job_list = [job["job_type"] for job in general_list]
    unic_job_list = [type_ for type_ in set(job_list)]

    return unic_job_list


def filter_by_job_type(jobs, job_type):
    job_list = [job for job in jobs if job["job_type"] == job_type]

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
    return job_list


def get_unique_industries(path):
    general_list = read(path)

    industry_list = [industry["industry"] for industry in general_list]
    unic_industry_list = [ind for ind in set(industry_list) if ind != ""]

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
    return unic_industry_list


def filter_by_industry(jobs, industry):
    unic_element = [unic for unic in jobs if unic["industry"] == industry]

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
    return unic_element


def get_max_salary(path):
    list = read(path)
    salary_list = [
        salary["max_salary"]
        for salary in list
        if salary["max_salary"] != "invalid"
    ]
    no_alone = [element for element in salary_list if element != ""]
    int_elements = [int(sal) for sal in no_alone]
    maximum = max(int_elements)
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
    return maximum


def get_min_salary(path):
    list = read(path)
    salary_list = [
        salary["min_salary"]
        for salary in list
        if salary["min_salary"] != "invalid"
    ]
    no_alone = [element for element in salary_list if element != ""]
    int_elements = [int(sal) for sal in no_alone]
    minimum = min(int_elements)

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
    return minimum


def matches_salary_range(job, salary):
    try:
        if job["max_salary"] < job["min_salary"] or type(salary) != int:
            raise ValueError

        if int(job["max_salary"]) >= int(salary) >= int(job["min_salary"]):
            return True

    except (ArithmeticError, KeyError, TypeError, ValueError):
        raise ValueError
    return False


def filter_by_salary_range(jobs, salary):
    new_list = [i for i in jobs if i["max_salary"] > i[
        "min_salary"] and type(salary) == int]
    print(new_list)
    try:
        filtered_list = [
            job for job in new_list
            if matches_salary_range(job, salary)
        ]
    except (ArithmeticError, KeyError, TypeError, ValueError):
        raise ValueError
    finally:
        return filtered_list
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
