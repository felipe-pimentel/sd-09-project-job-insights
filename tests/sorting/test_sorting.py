from src.sorting import sort_by

jobs = [
    {
        'name': 'junior',
        'min_salary': 1000,
        'max_salary': 2000,
        'date_posted': '2021-01-01'
    },
    {
        'name': 'pleno',
        'min_salary': 2001,
        'max_salary': 3000,
        'date_posted': '2021-02-01'
    },
    {
        'name': 'senior',
        'min_salary': 3001,
        'max_salary': 4000,
        'date_posted': '2021-03-01'
    }
]

order_by_min_salary = [
    {
        'name': 'junior',
        'min_salary': 1000,
        'max_salary': 2000,
        'date_posted': '2021-01-01'
    },
    {
        'name': 'pleno',
        'min_salary': 2001,
        'max_salary': 3000,
        'date_posted': '2021-02-01'
    },
    {
        'name': 'senior',
        'min_salary': 3001,
        'max_salary': 4000,
        'date_posted': '2021-03-01'
    }
]

order_by_max_salary = [
    {
        'name': 'senior',
        'min_salary': 3001,
        'max_salary': 4000,
        'date_posted': '2021-03-01'
    },
    {
        'name': 'pleno',
        'min_salary': 2001,
        'max_salary': 3000,
        'date_posted': '2021-02-01'
    },
    {
        'name': 'junior',
        'min_salary': 1000,
        'max_salary': 2000,
        'date_posted': '2021-01-01'
    },
]

order_by_date_posted = [
    {
        'name': 'senior',
        'min_salary': 3001,
        'max_salary': 4000,
        'date_posted': '2021-03-01'
    },
    {
        'name': 'pleno',
        'min_salary': 2001,
        'max_salary': 3000,
        'date_posted': '2021-02-01'
    },
    {
        'name': 'junior',
        'min_salary': 1000,
        'max_salary': 2000,
        'date_posted': '2021-01-01'
    },
]

criteria = ['min_salary', 'max_salary', 'date_posted']


def test_sort_by_criteria():
    sort_by(jobs, criteria[0])
    assert jobs == order_by_min_salary

    sort_by(jobs, criteria[1])
    assert jobs == order_by_max_salary

    sort_by(jobs, criteria[2])
    assert jobs == order_by_date_posted
