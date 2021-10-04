from src.sorting import sort_by

jobs = [
    {
        'type': 0,
        'max_salary': 4000,
        'min_salary': 3500,
        'date_posted': '2021-10-10'
    },
    {
        'type': 1,
        'max_salary': 5000,
        'min_salary': 4100,
        'date_posted': '2021-11-11'
    },
    {
        'type': 2,
        'max_salary': 6000,
        'min_salary': 5100,
        'date_posted': '2021-12-12'
    }
]

jobs_by_max = [
    {
        'type': 2,
        'max_salary': 6000,
        'min_salary': 5100,
        'date_posted': '2021-12-12'
    },
    {
        'type': 1,
        'max_salary': 5000,
        'min_salary': 4100,
        'date_posted': '2021-11-11'
    },
    {
        'type': 0,
        'max_salary': 4000,
        'min_salary': 3500,
        'date_posted': '2021-10-10'
    }
]

jobs_by_min = [
    {
        'type': 0,
        'max_salary': 4000,
        'min_salary': 3500,
        'date_posted': '2021-10-10'
    },
    {
        'type': 1,
        'max_salary': 5000,
        'min_salary': 4100,
        'date_posted': '2021-11-11'
    },
    {
        'type': 2,
        'max_salary': 6000,
        'min_salary': 5100,
        'date_posted': '2021-12-12'
    }
]

jobs_by_date = [
    {
        'type': 2,
        'max_salary': 6000,
        'min_salary': 5100,
        'date_posted': '2021-12-12'
    },
    {
        'type': 1,
        'max_salary': 5000,
        'min_salary': 4100,
        'date_posted': '2021-11-11'
    },
    {
        'type': 0,
        'max_salary': 4000,
        'min_salary': 3500,
        'date_posted': '2021-10-10'
    }
]

criteria = ['max_salary', 'min_salary', 'date_posted']


def test_sort_by_criteria():

    sort_by(jobs, criteria[0])
    assert jobs == jobs_by_max

    sort_by(jobs, criteria[1])
    assert jobs == jobs_by_min

    sort_by(jobs, criteria[2])
    assert jobs == jobs_by_date

# nome do teste segundo o readme: test_sorting_by_criteria
