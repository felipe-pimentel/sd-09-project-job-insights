from src.jobs import read

g_read = read('/media/luvecaro/101C902A1C900D3A/trybe/computer-science/projects/sd-09-project-job-insights/src/jobs.csv')


def get_unique_job_types(path):
    jobs_data = read(path)
    job_type_list = []

    for job in jobs_data:
        if job["job_type"] not in job_type_list:
            job_type_list.append(job["job_type"])

    return job_type_list


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []

    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs

# print(filter_by_job_type(g_read, ''))


def get_unique_industries(path):
    jobs_data = read(path)
    industry_list = []

    for job in jobs_data:
        if job["industry"] not in industry_list and job["industry"] != "":
            print(job["industry"])
            industry_list.append(job["industry"])

    return industry_list

# print(get_unique_industries('/media/luvecaro/101C902A1C900D3A/trybe/computer-science/projects/sd-09-project-job-insights/src/jobs.csv'))


def filter_by_industry(jobs, industry):
    filtered_industries = []

    for job in jobs:
        if job["industry"] == industry:
            filtered_industries.append(job)

    return filtered_industries


# print(filter_by_industry(g_read, 'Finance'))


def get_max_salary(path):
    jobs_data = read(path)
    max_salary_list = []

    for job in jobs_data:
        if job["max_salary"].isdigit():
            max_salary_list.append(int(float(job["max_salary"])))

    return max(max_salary_list)

# print(get_max_salary('/media/luvecaro/101C902A1C900D3A/trybe/computer-science/projects/sd-09-project-job-insights/src/jobs.csv'))


def get_min_salary(path):
    jobs_data = read(path)
    min_salary_list = []

    for job in jobs_data:
        if job["min_salary"].isdigit():
            min_salary_list.append(int(float(job["min_salary"])))

    return min(min_salary_list)

# print(get_min_salary('/media/luvecaro/101C902A1C900D3A/trybe/computer-science/projects/sd-09-project-job-insights/src/jobs.csv'))


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job or
        "max_salary" not in job or
        type(salary) != int or
        type(job["min_salary"]) != int or
        type(job["max_salary"]) != int or
        job["min_salary"] > job["max_salary"]
    ):
        raise ValueError("bad request")

    return (job["min_salary"] <= salary < job["max_salary"])


def filter_by_salary_range(jobs, salary):
    filtered_jobs_by_salary = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary) is True:
                filtered_jobs_by_salary.append(job)
        except ValueError:
            continue

    return filtered_jobs_by_salary
