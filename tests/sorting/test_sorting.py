# Para execução desse requisito tirei dúvidas com os PRs
# do Tiago Yoneda e Layo Kaminski
#


from src.sorting import sort_by


def test_sort_by_criteria():
    data = [
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "2021-09-11"},
        {"min_salary": 5000, "max_salary": 7000, "date_posted": "2021-09-01"},
        {"min_salary": 3000, "max_salary": 4000, "date_posted": "2021-09-15"},
        {"min_salary": 8000, "max_salary": 9000, "date_posted": "2021-09-05"},
        {"min_salary": 2000, "max_salary": 5000, "date_posted": "2021-09-03"},
        {"min_salary": 4000, "max_salary": 6000, "date_posted": "2021-09-10"}
    ]

    min_salary = [
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "2021-09-11"},
        {"min_salary": 2000, "max_salary": 5000, "date_posted": "2021-09-03"},
        {"min_salary": 3000, "max_salary": 4000, "date_posted": "2021-09-15"},
        {"min_salary": 4000, "max_salary": 6000, "date_posted": "2021-09-10"},
        {"min_salary": 5000, "max_salary": 7000, "date_posted": "2021-09-01"},
        {"min_salary": 8000, "max_salary": 9000, "date_posted": "2021-09-05"}
    ]

    max_salary = [
        {"min_salary": 8000, "max_salary": 9000, "date_posted": "2021-09-05"},
        {"min_salary": 5000, "max_salary": 7000, "date_posted": "2021-09-01"},
        {"min_salary": 4000, "max_salary": 6000, "date_posted": "2021-09-10"},
        {"min_salary": 2000, "max_salary": 5000, "date_posted": "2021-09-03"},
        {"min_salary": 3000, "max_salary": 4000, "date_posted": "2021-09-15"},
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "2021-09-11"},
    ]

    max_salary = [
        {"min_salary": 8000, "max_salary": 9000, "date_posted": "2021-09-05"},
        {"min_salary": 5000, "max_salary": 7000, "date_posted": "2021-09-01"},
        {"min_salary": 4000, "max_salary": 6000, "date_posted": "2021-09-10"},
        {"min_salary": 2000, "max_salary": 5000, "date_posted": "2021-09-03"},
        {"min_salary": 3000, "max_salary": 4000, "date_posted": "2021-09-15"},
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "2021-09-11"},
    ]

    date_posted = [
        {"min_salary": 3000, "max_salary": 4000, "date_posted": "2021-09-15"},
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "2021-09-11"},
        {"min_salary": 4000, "max_salary": 6000, "date_posted": "2021-09-10"},
        {"min_salary": 8000, "max_salary": 9000, "date_posted": "2021-09-05"},
        {"min_salary": 2000, "max_salary": 5000, "date_posted": "2021-09-03"},
        {"min_salary": 5000, "max_salary": 7000, "date_posted": "2021-09-01"},
    ]

    sort_by(data, "min_salary")
    assert data == min_salary

    sort_by(data, "max_salary")
    assert data == max_salary

    sort_by(data, "date_posted")
    assert data == date_posted
