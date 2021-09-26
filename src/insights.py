from src.jobs import read


def get_unique_job_types(path):

    readed_jobs = read(path)

    unique_jobs = set()
    for jobs in readed_jobs:
        unique_jobs.add(jobs['job_type'])
    return unique_jobs


# get_unique_job_types("jobs.csv")


def filter_by_job_type(jobs, job_type):

    jobs_to_return = []

    for job in jobs:
        if job_type == job['job_type']:
            jobs_to_return.append(job)
    return jobs_to_return


def get_unique_industries(path):

    readed_jobs = read(path)

    unique_industries = set()
    for jobs in readed_jobs:
        if jobs['industry'] != '':
            unique_industries.add(jobs['industry'])
    return unique_industries


# get_unique_industries("jobs.csv")


def filter_by_industry(jobs, industry):

    jobs_to_return = []

    for job in jobs:
        if industry == job['industry']:
            jobs_to_return.append(job)
    return jobs_to_return


def get_max_salary(path):

    readed_jobs = read(path)

    salary = 0
    for jobs in readed_jobs:
        if jobs['max_salary'].isdigit() and int(jobs['max_salary']) > salary:
            salary = int(jobs['max_salary'])
    return salary


def get_min_salary(path):

    readed_jobs = read(path)

    salary = 1000000
    for jobs in readed_jobs:
        if jobs['min_salary'].isdigit() and int(jobs['min_salary']) < salary:
            salary = int(jobs['min_salary'])
    return salary


# get_min_salary('jobs.csv')


def matches_salary_range(job, salary):
    # https://www.geeksforgeeks.org/python-get-dictionary-keys-as-a-list/
    if 'min_salary' not in job.keys() or 'max_salary' not in job.keys():
        raise ValueError("min_salary or max_salary doens't exist")
    if type(job['min_salary']) != int or type(
            job['max_salary']) != int or type(salary) != int:
        raise ValueError("min_salary and max_salary must be numbers")
    if job['min_salary'] > job['max_salary']:
        raise ValueError("min_salary can't be higher than max_salary")
    if job['min_salary'] <= salary <= job['max_salary']:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):

    jobs_to_return = []

    for job in jobs:
        if job['min_salary'] > job['max_salary'] or type(salary) != int:
            pass
        elif job['min_salary'] <= salary <= job['max_salary']:
            jobs_to_return.append(job)
    return jobs_to_return
