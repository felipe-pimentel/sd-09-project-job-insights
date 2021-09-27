from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"min_salary": 200, "max_salary": 6000, "date_posted": "2021-05-25"},
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "2021-05-10"},
        {"min_salary": 3000, "max_salary": 9000, "date_posted": "2021-05-22"},
    ]

    sort_by(jobs, 'max_salary')
    lista = []
    for job in jobs:
        lista.append(job['max_salary'])
    assert lista == [9000, 6000, 3000]

    sort_by(jobs, 'min_salary')
    lista = []
    for job in jobs:
        lista.append(job['min_salary'])
    assert lista == [200, 1000, 3000]

    sort_by(jobs, 'date_posted')
    lista = []
    for job in jobs:
        lista.append(job['date_posted'])
    assert lista == ["2021-05-25", "2021-05-22", "2021-05-10"]
