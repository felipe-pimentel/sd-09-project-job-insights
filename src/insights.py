def get_unique_job_types(path):
    from src.jobs import read

    jobs_read = read(path)

    job_types = []
    for job in jobs_read:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = [job for job in jobs if job["job_type"] in job_type]
    return filtered_jobs


def get_unique_industries(path):
    from src.jobs import read

    jobs_read = read(path)

    industries = []
    for job in jobs_read:
        if job["industry"] not in industries and job["industry"] != '':
            industries.append(job["industry"])

    return industries


def filter_by_industry(jobs, industry):
    filtered_industries = [job for job in jobs if job["industry"] in industry]
    return filtered_industries


def get_max_salary(path):
    from src.jobs import read

    jobs_read = read(path)

    max_salaries = []
    for job in jobs_read:
        if job["max_salary"] not in max_salaries and job["max_salary"] != '':
            try:
                converted_number = float(job["max_salary"])
            except ValueError:
                pass
            else:
                max_salaries.append(converted_number)

    return max(max_salaries)


def get_min_salary(path):
    from src.jobs import read

    jobs_read = read(path)

    min_salaries = []
    for job in jobs_read:
        if job["min_salary"] not in min_salaries and job["min_salary"] != '':
            try:
                converted_number = float(job["min_salary"])
            except ValueError:
                pass
            else:
                min_salaries.append(converted_number)

    return min(min_salaries)


def matches_salary_range(job, salary):
    try:
        min_salary_number = int(job["min_salary"])
        max_salary_number = int(job["max_salary"])
        salary_number = int(salary)
        if min_salary_number > max_salary_number:
            raise ValueError('invalid salary range')
        if min_salary_number <= salary_number <= max_salary_number:
            return True
        else:
            return False
    except TypeError:
        raise ValueError('wrong type of value')
    except KeyError:
        raise ValueError('missing input')
    except ValueError:
        raise ValueError('one of the inputs is not a number')


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
