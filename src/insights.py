import src.jobs


"""https://towardsdatascience.com/
how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c"""


def get_unique_job_types(path):
    jobs_list = src.jobs.read(path)
    result = set()
    for job in jobs_list:
        for type in job["job_type"].split(","):
            result.add(type)
    return result


def filter_by_job_type(jobs, job_type):
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
    result = []
    for job in jobs:
        try:
            if job["job_type"] == job_type:
                result.append(job)
        except TypeError:
            # print("Campo inválido")
            pass
    return result


def get_unique_industries(path):
    jobs_list = src.jobs.read(path)
    result = set()
    for job in jobs_list:
        try:
            if job["industry"] != "":
                result.add(job["industry"])
        except ValueError:
            # print("Campo inválido")
            pass
    return result


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
    result = []
    for job in jobs:
        try:
            if job["industry"] == industry:
                result.append(job)
        except TypeError:
            # print("Campo inválido")
            pass
    return result


def get_max_salary(path):
    jobs_list = src.jobs.read(path)
    result = set()
    for job in jobs_list:
        try:
            if job["max_salary"] != "":
                result.add(int(job["max_salary"]))
        except ValueError:
            # print('Campo inválido')
            pass
    return max(result)


def get_min_salary(path):
    jobs_list = src.jobs.read(path)
    result = set()
    for job in jobs_list:
        try:
            if job["min_salary"] != "":
                result.add(int(job["min_salary"]))
        except ValueError:
            print('Campo inválido')
    return min(result)


def matches_salary_range(job, salary):
    try:
        if int(job['min_salary'] > job['max_salary']):
            raise ValueError
        elif int(job['min_salary']) <= int(salary) <= int(job['max_salary']):
            return True
        else:
            return False
    except (TypeError, ValueError, KeyError):
        raise ValueError
# depois de muito lutar com esse requisito, conseguimos chegar em
# um resultado muito enxuto que engloba os casos de erros.
# O Carlos me ajudou MUITO a entender melhor o que estava ocorrendo
# e conseguimos solucionar. O try vai tentar definir se o parâmetro
# salary está dentro da faixa salarial da vaga em questão e qualquer
# erro que ocorrer nessa verificação é tratado no except logo abaixo.
# Se os valores estiverem corretos, se os campos estiverem presentes
# e válidos, etc etc, a função compara o salary e retorna True ou
# False. Todos os outros casos levantam o ValueError


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
