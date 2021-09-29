from src.jobs import read
# from jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    unique_jobs = []
    for job in jobs_list:
        if job['job_type'] not in unique_jobs:
            unique_jobs.append(job['job_type'])
    return unique_jobs
    # unique_jobs = []
    # unique_job_type = {}
    # for job in jobs_list:
    #     if job['job_type'] not in unique_job_type:
    #         # unique_jobs.append(job)
    #         unique_job_type[job['job_type']] = {'jobs': 0}
    #     unique_job_type[job['job_type']]['jobs'] += 1
    # print(unique_job_type)
    # return unique_job_type


def filter_by_job_type(jobs, job_type):
    jobs_filtered = [job for job in jobs if job['job_type'] == job_type]
    return jobs_filtered


def get_unique_industries(path):
    jobs_list = read(path)
    unique_industries = []
    for job in jobs_list:
        if job['industry'] not in unique_industries and job['industry'] != '':
            unique_industries.append(job['industry'])
    return unique_industries


# get_unique_industries('jobs.csv')


def filter_by_industry(jobs, industry):
    jobs_filtered = [job for job in jobs if job['industry'] == industry]
    return jobs_filtered


def get_max_salary(path):
    jobs_list = read(path)
    max_salary = 0
    for job in jobs_list:
        valid = job['max_salary'] != '' and job['max_salary'] != 'invalid'
        if valid and int(job['max_salary']) > max_salary:
            max_salary = int(job['max_salary'])
    return max_salary


def get_min_salary(path):
    jobs_list = read(path)
    min_salary = 0
    for job in jobs_list:
        valid = job['min_salary'] != '' and job['min_salary'] != 'invalid'
        if valid and (int(job['min_salary']) < min_salary or min_salary == 0):
            min_salary = int(job['min_salary'])
    return min_salary


def matches_salary_range(job, salary):
    if (
        'min_salary' not in job or
        type(job['min_salary']) != int or
        job['max_salary'] == '' or
        type(job['max_salary']) != int or
        type(salary) != int or
        job['min_salary'] > job['max_salary']
    ):
        raise ValueError("bad request")
    return job['max_salary'] > salary >= job['min_salary']


def filter_by_salary_range(jobs, salary):
    jobs_filtered = []
    for job in jobs:
        valid_min = 'min_salary' in job and type(job['min_salary'] == int)
        valid_max = 'max_salary' in job and type(job['max_salary'] == int)
        valid_range = job['max_salary'] > job['min_salary']
        valid_salary = type(salary) == int
        valid = valid_max and valid_min and valid_range and valid_salary
        if valid:
            job_dict = {
                'min_salary': job['min_salary'],
                'max_salary': job['max_salary']}
            if matches_salary_range(job_dict, salary):
                jobs_filtered.append(job)
    return jobs_filtered
