from src.jobs import read


def get_unique_job_types(path):
    lista = read(path)
    jobtypes = []

    for row in lista:
        if row['job_type'] != '' and row['job_type'] not in jobtypes:
            jobtypes.append(row['job_type'])

    return jobtypes


def filter_by_job_type(jobs, job_type):
    filter = []

    for row in jobs:
        if row["job_type"] == job_type:
            filter.append(row)

    return filter


def get_unique_industries(path):
    lista = read(path)

    industries = set()

    for row in lista:
        if row["industry"] != "":
            industries.add(row["industry"])

    return industries


def filter_by_industry(jobs, industry):
    filter = []

    for row in jobs:
        if row["industry"] == industry:
            filter.append(row)

    return filter


def get_max_salary(path):
    lista = read(path)
    empty = []
    for row in lista:
        if row["max_salary"].isdigit():
            empty.append(int(row["max_salary"]))

    return max(empty)


def get_min_salary(path):
    lista = read(path)
    empty = []
    for row in lista:
        if row["min_salary"].isdigit():
            empty.append(int(row["min_salary"]))

    return min(empty)


def matches_salary_range(job, salary):
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError('Salário não existe')
    else:
        min_salary = job['min_salary']
        max_salary = job['max_salary']
    if not (isinstance(min_salary, int) and isinstance(max_salary, int)):
        raise ValueError("O salário não é valido")
    if min_salary > max_salary:
        raise ValueError('O salário mínimo é maior que o máximo')
    if min_salary <= salary <= max_salary:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    list = []
    for row in jobs:
        max = int(row['max_salary'])
        min = int(row['min_salary'])
        if isinstance(salary, int):
            if isinstance(max, int) and isinstance(max, int):
                if min <= salary <= max:
                    list.append(row)
    return list

# Última função estava dando um erro, TypeError: '<=' not supported between instances of 'int' and 'NoneType'
# Solução foi passar os salarios para int, encontrada no repositório: https://github.com/tryber/sd-08-project-job-insights/pull/23/files