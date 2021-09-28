from src.sorting import sort_by


def test_sort_by_criteria():
    pass
    test_1 = [
        {
            'name': 'job_1',
            'min_salary': 1000,
            'max_salary': 2000,
            'date_posted': '2021-02-26'
        },
        {
            'name': 'job_2',
            'min_salary': 3000,
            'max_salary': 4000,
            'date_posted': '2021-02-27'
        },
        {
            'name': 'job_3',
            'min_salary': 5000,
            'max_salary': 6000,
            'date_posted': '2021-02-28'
        }
    ]

    test_2 = [
        {
            'name': 'job_1',
            'min_salary': 1500,
            'max_salary': 3000,
            'date_posted': '2021-02-26'
        },
        {
            'name': 'job_2',
            'min_salary': 300,
            'max_salary': 500,
            'date_posted': '2021-02-27'
        },
        {
            'name': 'job_3',
            'min_salary': 799,
            'max_salary': 1999,
            'date_posted': '2021-02-28'
        }
    ]

    test_3 = [
        {
            'name': 'job_1',
            'min_salary': 3333,
            'max_salary': 4444,
            'date_posted': '2021-02-28'
        },
        {
            'name': 'job_2',
            'min_salary': 5555,
            'max_salary': 6666,
            'date_posted': '2021-02-27'
        },
        {
            'name': 'job_3',
            'min_salary': 3232,
            'max_salary': 4343,
            'date_posted': '2021-02-26'
        }
    ]

    types = ['min_salary', 'max_salary', 'date_posted']

    for type in types:
        result = sort_by(test_1, type)
        if (type == 'min_salary'):
            assert result == test_2
        else:
            assert result == test_3
