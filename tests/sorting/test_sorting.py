from src.sorting import sort_by


# sory_by ( dicionario com jobs, uma string com 'criteria' )
# devemos testar as criteria ('min_salary', 'max_salary', 'date_posted')
# precisamos simular a entrada e ter a saida esperada
# chamar a funcao com a entrada e comparar com a saida
# date_posted tem formato yyyy-mm-dd
def test_sort_by_criteria():
    selected_criteria = ["min_salary", "max_salary", "date_posted"]
    job_1 = {
        "job_name": "Diesel Mechanic",
        "min_salary": 46298,
        "max_salary": 55893,
        "date_posted": "2021-09-09",
    }
    job_2 = {
        "job_name": "JUltrasound Technologist",
        "min_salary": 55069,
        "max_salary": 74745,
        "date_posted": "2021-02-02",
    }
    job_3 = {
        "job_name": "ABA Therapist",
        "min_salary": 20000,
        "max_salary": 35000,
        "date_posted": "2021-04-17",
    }
    job_4 = {
        "job_name": "Senior Salesforce Developer",
        "min_salary": 44587,
        "max_salary": 82162,
        "date_posted": "2021-04-05",
    }
    job_5 = {
        "job_name": "Emergency Veterinary Technician",
        "min_salary": 38471,
        "max_salary": 43006,
        "date_posted": "2021-01-05",
    }
    job_list = [job_1, job_2, job_3, job_4, job_5]

    min_salary_sort = [job_3, job_5, job_4, job_1, job_2]  # crescente
    max_salary_sort = [job_4, job_2, job_1, job_5, job_3]  # decrescente
    date_posted_sort = [job_1, job_3, job_4, job_2, job_5]  # decrescente
    # resultado esperado na mesma ordem que o criteria
    expected = [min_salary_sort, max_salary_sort, date_posted_sort]

    # lembrar que esse método sort altera
    for index in range(len(selected_criteria)):
        sort_by(job_list, selected_criteria[index])  # muda o job_list
        assert job_list == expected[index]
