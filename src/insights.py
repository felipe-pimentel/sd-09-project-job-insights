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


def validate_salary(salary):
    test_salary = isinstance(salary, int)
    if not test_salary:
        raise ValueError('salary should be a number')

    pass


def validate_job(job):
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError('min_salary and max_salary is required')

    test_min_salary_key = isinstance(job['min_salary'], int)
    test_max_salary_key = isinstance(job['max_salary'], int)

    if not test_min_salary_key or not test_max_salary_key:
        raise ValueError('min_salary and max_salary should be a number')
    elif job['min_salary'] > job['max_salary']:
        raise ValueError('min_salary is bigger than max_salary')

    pass


def matches_salary_range(job, salary):
    validate_job(job)
    validate_salary(salary)

    if job['min_salary'] <= salary <= job['max_salary']:
        return True

    return False


def filter_by_salary_range(jobs, salary):
    jobs_by_salary = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_by_salary.append(job)
        except ValueError:
            pass
    return jobs_by_salary
