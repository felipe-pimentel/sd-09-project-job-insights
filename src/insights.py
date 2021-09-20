from src import jobs


def get_unique_job_types(path):
    all_jobs = jobs.read(path)
    output = []
    for job in all_jobs:
        if job["job_type"] not in output and job["job_type"] != '':
            output.append(job["job_type"])
    return output


def filter_by_job_type(jobs, job_type):
    output = []
    for job in jobs:
        if job['job_type'] == job_type:
            output.append(job)
    return output


def get_unique_industries(path):
    all_jobs = jobs.read(path)
    output = []
    for job in all_jobs:
        if job["industry"] not in output and job["industry"] != '':
            output.append(job["industry"])
    return output


def filter_by_industry(jobs, industry):
    output = []
    for job in jobs:
        if job['industry'] == industry:
            output.append(job)
    return output


def get_max_salary(path):
    all_jobs = jobs.read(path)
    output = []
    for job in all_jobs:
        if job["max_salary"] not in output and job["max_salary"] != '':
            try:
                output.append(int(job['max_salary']))
            except Exception:
                print("Error in converting")
    return max(output)


def get_min_salary(path):
    all_jobs = jobs.read(path)
    output = []
    for job in all_jobs:
        if job["min_salary"] not in output and job["min_salary"] != '':
            try:
                output.append(int(job['min_salary']))
            except Exception:
                print("Error in converting")
    return min(output)


def matches_salary_range(job, salary):
    try:
        if (int(job['max_salary']) < int(job['min_salary'])):
            raise ValueError("max_salary < min_salary ")
        return int(job['min_salary']) <= salary <= int(job['max_salary'])
    except Exception:
        raise ValueError(
            '''Some error with inputs...
        Or they are ausents,
         or they are incompatible''')


def filter_by_salary_range(jobs, salary):
    output = []
    for job in jobs:
        try:
            if (matches_salary_range(job, salary)):
                output.append(job)
        except Exception:
            print("Validation error")
    return output
