from jobs import read


def get_unique_job_types(path):
    job_type = set()
    list_categories = read(path)
    for jobs in list_categories:
        job_type.add(jobs["job_type"])
    return job_type


def filter_by_job_type(jobs, job_type):
    return lambda jobs: jobs.filter(job_type)


def get_unique_industries(path):
    industry_type = set()
    for industry in read(path):
        print(industry["industry"])
        industry_type.add(industry["industry"])
    return industry_type


def filter_by_industry(jobs, industry):
    pass


def get_max_salary(path):

    pass


def get_min_salary(path):

    pass


def matches_salary_range(job, salary):

    pass


def filter_by_salary_range(jobs, salary):

    return []
