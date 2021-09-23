from src.jobs import read


"""
2 - Implemente a função get_unique_job_types
local: src/insights.py

Agora que temos como carregar os dados, podemos começar a extrair informação
deles. Primeiro, vamos identificar quais tipos de empregos existem.
  A função deve receber o path do arquivo csv com os dados.
  A função deve invocar a função jobs.read com o path recebido para obter os
  dados.
  A função deve retornar uma lista de valores únicos presentes na coluna
  job_type.

O que será verificado pelo avaliador:
  A função carrega os dados do arquivo recebido como parâmetro
  A função retorna a quantidade correta de valores
  A função retorna os valores corretos
  A função desconsidera valores vazios
"""


def get_unique_job_types(path):
    data_jobs = read(path)
    jobs_types = set()
    for job in data_jobs:
        jobs_types.add(job["job_type"])
    return jobs_types


"""
6 - Implemente a função filter_by_job_type
local: src/insights.py

Os empregos estão listados em um aplicativo web. Para permitir que a pessoa
usuária possa filtrar os empregos por tipo de emprego, vamos precisar
implementar esse filtro.
    A função deve receber uma lista de dicionários jobs como primeiro
    parâmetro.
    A função deve receber uma string job_type como segundo parâmetro.
    A função deve retornar uma lista com todos os empregos onde a coluna jobs
    corresponde ao parâmetro job_type.

O que será verificado pelo avaliador:
    A função retorna a quantidade correta de valores
    A função retorna os valores corretos
    A função retorna os valores na ordem correta
    A função retorna uma lista vazia para job_types ausentes nos jobs recebidos
"""


def filter_by_job_type(jobs, job_type):
    job_list_by_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_list_by_type.append(job)
    return job_list_by_type


"""
3 - Implemente a função get_unique_industries
local: src/insights.py

Da mesma forma, agora iremos identificar quais indústrias estão representadas
nesse conjunto de dados.
  A função deve obter os dados da mesma forma que o requisito 2.
  A função deve retornar uma lista de valores únicos presentes na coluna
  industry.
  A função desconsidera valores vazios

O que será verificado pelo avaliador:
  A função carrega os dados do arquivo recebido como parâmetro
  A função retorna a quantidade correta de valores
  A função retorna os valores corretos
"""


def get_unique_industries(path):
    data_jobs = read(path)
    industries = set()
    for job in data_jobs:
        if job["industry"] != "":
            industries.add(job["industry"])
    return industries


"""
7 - Implemente a função filter_by_industry
local: src/insights.py

Do mesmo modo, o aplicativo precisa permitir uma filtragem por indústria.
Vamos precisar implementar esse filtro também.
    A função deve receber uma lista de dicionários jobs como primeiro
    parâmetro.
    A função deve receber uma string industry como segundo parâmetro.
    A função deve retornar uma lista de dicionários com todos os empregos onde
    a coluna jobs corresponde ao parâmetro industry.

O que será verificado pelo avaliador:
    A função retorna a quantidade correta de valores
    A função retorna os valores corretos
    A função retorna os valores na ordem correta
    A função retorna uma lista vazia para industry ausentes nos jobs recebidos
"""


def filter_by_industry(jobs, industry):
    job_list_by_industry = []
    for job in jobs:
        if job["industry"] == industry:
            job_list_by_industry.append(job)
    return job_list_by_industry


"""
4 - Implemente a função get_max_salary
local: src/insights.py

Os dados apresentam faixas salariais para cada emprego exibido. Vamos agora
encontrar o maior valor de todas as faixas.
    A função deve obter os dados da mesma forma que o requisito 2.
    A função deve ignorar os valores ausentes.
    A função deve retornar um valor inteiro com o maior salário presente na
    coluna max_salary.

O que será verificado pelo avaliador:
    A função carrega os dados do arquivo recebido como parâmetro
    A função retorna o valor correto
"""


def get_max_salary(path):
    data_jobs = read(path)
    salaries = set()
    for job in data_jobs:
        if job["max_salary"].isdigit():
            salaries.add(job["max_salary"])
    bigger_salary = int(max(salaries, key=int))
    return bigger_salary


"""
5 - Implemente a função get_min_salary
local: src/insights.py

Os dados apresentam faixas salariais para cada emprego exibido. Vamos agora
encontrar o menor valor de todas as faixas.
    A função deve obter os dados da mesma forma que o requisito 2.
    A função deve ignorar os valores ausentes.
    A função deve retornar um valor inteiro com o menor salário presente na
    coluna min_salary.

O que será verificado pelo avaliador:
    A função carrega os dados do arquivo recebido como parâmetro
    A função retorna o valor correto
"""


def get_min_salary(path):
    data_jobs = read(path)
    salaries = set()
    for job in data_jobs:
        if job["min_salary"].isdigit():
            salaries.add(job["min_salary"])
    smaller_salary = int(min(salaries, key=int))
    return smaller_salary


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
    pass


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
