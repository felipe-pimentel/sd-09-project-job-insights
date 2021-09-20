from src.jobs import read

# from functools import reduce


# def get_unique_job_types(path):
#     list_dict = read(path)
#     jobs_fiter = []
#     for job in list_dict:
#         if not job["job_type"] in jobs_fiter:
#             jobs_fiter.append(job["job_type"])
#     return jobs_fiter


# refatorado HOF
# mapeia somente as chaves jobs_type
# set transforma em conjunto sem repetir valores
def get_unique_job_types(path):
    list_dict = read(path)
    map_jobs = list(map(lambda el: el["job_type"], list_dict))
    new_list = list(set(map_jobs))
    return new_list


# def filter_by_job_type(jobs, job_type):
#     jobs_filter = []
#     for job in jobs:
#         if job["job_type"] == job_type:
#             jobs_filter.append(job)
#     return jobs_filter

# Refatorado HOF
def filter_by_job_type(jobs, job_type):
    return list(filter(lambda el: el["job_type"] == job_type, jobs))


# def get_unique_industries(path):
#     list_dict = read(path)
#     ind_filter = []
#     for ind in list_dict:
#         if not ind["industry"] in ind_filter and ind["industry"] != "":
#             ind_filter.append(ind["industry"])
#     print(ind_filter)
#     return ind_filter


# refatorado HOF
def get_unique_industries(path):
    list_dict = read(path)
    filter_ind = list(filter(lambda el: el["industry"] != "", list_dict))
    map_ind = list(map(lambda el: el["industry"], filter_ind))
    new_list = list(set(map_ind))
    return new_list


# def filter_by_industry(jobs, industry):
#     job_filter_by_ind = []
#     for job in jobs:
#         if job["industry"] == industry:
#             job_filter_by_ind.append(job)
#     return job_filter_by_ind

# Refatorado HOF
def filter_by_industry(jobs, industry):
    return list(filter(lambda el: el["industry"] == industry, jobs))


# def get_max_salary(path):
#     list_dict = read(path)
#     salary_max = 0
#     salary_list = []

#     for salary in list_dict:
#         if salary["max_salary"].isdigit():
#             salary_list.append(int(salary["max_salary"]))

#     for salary in salary_list:
#         if salary > salary_max:
#             salary_max = salary
#     print(salary_max)

#     return salary_max


# Refatorado HOF
# filtra sal. q são numeros / mapeia só sal e converte para int / busca max
def get_max_salary(path):
    list_dict = read(path)
    filter_salary = list(
        filter(lambda el: el["max_salary"].isdigit(), list_dict)
    )
    map_salary = list(map(lambda el: int(el["max_salary"]), filter_salary))
    max_salarary = max(map_salary)
    return max_salarary


# def get_min_salary(path):
#     list_dict = read(path)
#     salary_min = 100000
#     salary_list = []

#     for salary in list_dict:
#         if salary["min_salary"].isdigit():
#             salary_list.append(int(salary["min_salary"]))

#     for salary in salary_list:
#         if salary < salary_min:
#             salary_min = salary
#     print(salary_min)
#     return salary_min


# Refatorado HOF
def get_min_salary(path):
    list_dict = read(path)
    filter_salary = list(
        filter(lambda el: el["min_salary"].isdigit(), list_dict)
    )
    map_salary = list(map(lambda el: int(el["min_salary"]), filter_salary))
    min_salarary = min(map_salary)
    return min_salarary


def matches_salary_range(job, salary):
    if not ("min_salary" in job and "max_salary" in job):
        raise ValueError(
            "job['min_salary'] or job['max_salary'] doesn't exists"
        )
    elif not (
        type(job["min_salary"]) is int or type(job["max_salary"]) is int
    ):
        raise ValueError(
            "job['min_salary'] or job['max_salary'] aren't valid integers"
        )
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError(
            "job['min_salary'] is greather than job['max_salary']"
        )
    elif not (type(salary) is int):
        raise ValueError("salary isn't a valid integer")
    else:
        return job["min_salary"] <= salary <= job["max_salary"]


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
