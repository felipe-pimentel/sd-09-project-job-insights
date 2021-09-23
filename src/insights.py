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


"""
8 - Implemente a função matches_salary_range
local: src/insights.py

O aplicativo vai precisar filtrar os empregos por salário também. Como uma
função auxiliar, implemente matches_salary_range para conferir que o salário
procurado está dentro da faixa salarial daquele emprego. Vamos aproveitar
também para conferir se a faixa salarial faz sentido -- isto é, se o valor
mínimo é menor que o valor máximo.
    A função deve receber um dicionário job como primeiro parâmetro, com as
    chaves min_salary e max_salary.
    A função deve receber um inteiro salary como segundo parâmetro.
    A função deve lançar um erro ValueError nos seguintes casos:
        alguma das chaves min_salary ou max_salary estão ausentes no
        dicionário;
        alguma das chaves min_salary ou max_salary tem valores não-numéricos;
        o valor de min_salary é maior que o valor de max_salary;
        o parâmetro salary tem valores não-numéricos;
    A função deve retornar True se o salário procurado estiver dentro da faixa
    salarial ou False se não estiver.

O que será verificado pelo avaliador:
    A função retorna o booleano correto
    A função lança um ValueError se o valor de min_salary for maior que o
    valor de max_salary
    A função lança um ValueError se as chaves min_salary ou max_salary tiverem
    valores não numéricos
    A função lança um ValueError se o parâmetro salary tiver valor não numérico
    A função lança um ValueError se as chaves min_salary ou max_salary
    estiverem ausentes no dicionário
"""


def matches_salary_range(job, salary):
    if "max_salary" not in job.keys() or "min_salary" not in job.keys():
        raise ValueError("min_salary or max_salary keys are missing")

    max_salary = type(job["max_salary"]) is not int
    min_salary = type(job["min_salary"]) is not int

    if min_salary or max_salary:
        raise ValueError("min_salary or max_salary values ​​are not integers")
    elif job["max_salary"] < job["min_salary"]:
        raise ValueError(
            "the minimum salary is greater than the maximum salary"
        )
    elif not type(salary) is int:
        raise ValueError("salary is not a valid integer value")
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
