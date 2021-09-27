"""
10 - Implemente um teste para a função sort_by
local: tests/sorting/test_sorting.py

Por fim, espera-se que a pessoa usuária possa escolher um critério de
ordenação para exibir os empregos. Já temos uma implementação para essa
ordenação em src/sorting.py, mas queremos ter certeza de que ela funciona e,
principalmente, que não deixará de funcionar conforme vamos implementando
novos recursos. Precisamos então escrever um teste!

Esse teste deve se chamar test_sorting_by_criteria e garantir que a função
funciona segundo esta especificação:
  A função sort_by recebe dois parâmetros:
    jobs uma lista de dicionários com os detalhes de cada emprego;
    criteria uma string com uma chave para ser usada como critério de
    ordenação.
  O parâmetro criteria deve ter um destes valores: min_salary, max_salary,
  date_posted
  A ordenação para min_salary deve ser crescente, mas para max_salary ou
  date_posted devem ser decrescentes.
  Os empregos que não apresentarem um valor válido no campo escolhido para
  ordenação devem aparecer no final da lista.
  ** O teste da Trybe espera que o seu teste falhe em alguns casos. Nesse caso,
  o teste terá a saída XFAIL (ao invés de PASS ou FAIL), e isso significa que
  o requisito foi atendido heavy_check_mark

O que será verificado pelo avaliador:
  O teste rejeita implementações que aceitam critérios não especificados.
  O teste rejeita implementações que não ordenam corretamente.
  O teste rejeita implementações que não ordenam em ordem crescente quando o
  critério é min_salary.
  O teste aprova implementações corretas.
"""


# from src.sorting import sort_by
from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "02-11-1995"},
        {"min_salary": 3001, "max_salary": 6000, "date_posted": "05-23-1998"},
        {"min_salary": 950, "max_salary": 10000, "date_posted": "08-01-2002"},
    ]

    jobs_min_salary = [
        {"min_salary": 950, "max_salary": 10000, "date_posted": "08-01-2002"},
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "02-11-1995"},
        {"min_salary": 3001, "max_salary": 6000, "date_posted": "05-23-1998"},
    ]

    jobs_max_salary = [
        {"min_salary": 950, "max_salary": 10000, "date_posted": "08-01-2002"},
        {"min_salary": 3001, "max_salary": 6000, "date_posted": "05-23-1998"},
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "02-11-1995"},
    ]

    jobs_date_posted = [
        {"min_salary": 950, "max_salary": 10000, "date_posted": "08-01-2002"},
        {"min_salary": 3001, "max_salary": 6000, "date_posted": "05-23-1998"},
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "02-11-1995"},
    ]

    sort_by(jobs, "min_salary")
    assert jobs == jobs_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == jobs_max_salary

    sort_by(jobs, "date_posted")
    assert jobs == jobs_date_posted
