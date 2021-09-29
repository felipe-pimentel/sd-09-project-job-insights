from src.sorting import sort_by

jobs = [
    {
        'min_salary': 2000,
        'max_salary': 3000,
    },
    {
        'min_salary': 0,
        'max_salary': 1000,
    },
    {
        'min_salary': 4000,
        'max_salary': 5000,
    }
]

jobs_order_by_min_salary = [
    {
        'min_salary': 0,
        'max_salary': 1000,
    },
    {
        'min_salary': 2000,
        'max_salary': 3000,
    },
    {
        'min_salary': 4000,
        'max_salary': 5000,
    }
]

jobs_order_by_max_salary = [
    {
        'min_salary': 4000,
        'max_salary': 5000,
    },
    {
        'min_salary': 2000,
        'max_salary': 3000,
    },
    {
        'min_salary': 0,
        'max_salary': 1000,
    },
]


def test_sort_by_criteria():
    sort_by(jobs, 'min_salary')
    assert jobs == jobs_order_by_min_salary

    sort_by(jobs, 'max_salary')
    assert jobs == jobs_order_by_max_salary
