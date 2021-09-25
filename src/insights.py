from src.jobs import read


def get_unique_job_types(path):
    #  REQ 02
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs = read(path)
    file_data = set()  # set retorna dados únicos
    for job in jobs:
        file_data.add(job['job_type'])  # job_type é a coluna
    return file_data


def filter_by_job_type(jobs, job_type):
    #  REQ 06
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
    # EXEMPLO 02 - filter tem 2 argumentos (função - iterável)
    # https://www.programiz.com/python-programming/methods/built-in/filter
    return list(filter(lambda job: job["job_type"] == job_type, jobs))


def get_unique_industries(path):
    #  REQ 03
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
    jobs = read(path)
    file_data = set()  # set retorna dados únicos
    for job in jobs:
        if job["industry"] != "":
            file_data.add(job["industry"])
    return file_data


def filter_by_industry(jobs, industry):
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
    return list(filter(lambda job: job["industry"] == industry, jobs))


def get_max_salary(path):
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
    #  https://www.programiz.com/python-programming/methods/string/isnumeric
    #  https://www.programiz.com/python-programming/methods/built-in/max
    jobs = read(path)
    highest_salary = set()
    for job in jobs:
        if job["max_salary"].isnumeric():
            highest_salary.add(int(job["max_salary"]))

    return max(highest_salary)


def get_min_salary(path):
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

    #  https://www.programiz.com/python-programming/methods/string/isnumeric
    #  https://www.programiz.com/python-programming/methods/built-in/min
    jobs = read(path)
    lowest_salary = set()
    for job in jobs:
        if job["min_salary"].isnumeric():
            lowest_salary.add(int(job["min_salary"]))

    return min(lowest_salary)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    #  O keys()método retorna um objeto de visualização.
    #  O objeto de visualização contém as chaves do dicionário, como uma lista.
    #  https://www.w3schools.com/python/ref_dictionary_keys.asp
    #  https://www.programiz.com/python-programming/methods/built-in/isinstance
    if not (
        "min_salary" in job.keys()
        and isinstance(job["min_salary"], int)
        and job["min_salary"] >= 0
    ):
        raise ValueError("Erro ao encontrar o min_salary")

    if not (
        "max_salary" in job.keys()
        and isinstance(job["max_salary"], int)
        and job["max_salary"] >= 0
    ):
        raise ValueError("Erro ao encontrar o max_salary")

    if job["min_salary"] > job["max_salary"]:
        raise ValueError("Erro, o min_salary é maior que o max_salary")

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
    #  https://www.programiz.com/python-programming/methods/dictionary/keys
    #  O método keys () retorna um objeto de visualização que exibe
    #  uma lista de todas as chaves no dicionário
    filter_salary_range = []

    for job in jobs:
        if (
            isinstance(salary, int)
            and ("min_salary" in job.keys() and "max_salary" in job.keys())
            and isinstance(job["max_salary"], int)
            and isinstance(job["min_salary"], int)
            and int(job["min_salary"]) >= 0 and int(job["max_salary"]) >= 0
            and int(job["min_salary"]) <= int(job["max_salary"])
            and matches_salary_range(job, salary)
        ):
            filter_salary_range.append(job)
            #  método anexa um elemento ao final da lista

    return filter_salary_range
