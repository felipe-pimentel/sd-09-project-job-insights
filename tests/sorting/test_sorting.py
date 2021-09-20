from src.sorting import sort_by


def test_sort_by_criteria():

    jobs_group = [
        {
            'name': 'avraw',
            'min_salary': 100,
            'max_salary': 220,
            'date_posted': '2021-02-26'
        },
        {
            'name': 'bvraw',
            'min_salary': 110,
            'max_salary': 210,
            'date_posted': '2021-02-27'
        },
        {
            'name': 'cvraw',
            'min_salary': 120,
            'max_salary': 200,
            'date_posted': '2021-02-28'
        }
    ]

    jobs_group1 = [
        {
            'name': 'avraw',
            'min_salary': 100,
            'max_salary': 220,
            'date_posted': '2021-02-26'
        },
        {
            'name': 'bvraw',
            'min_salary': 110,
            'max_salary': 210,
            'date_posted': '2021-02-27'
        },
        {
            'name': 'cvraw',
            'min_salary': 120,
            'max_salary': 200,
            'date_posted': '2021-02-28'
        }
    ]

    jobs_group2 = [
        {
            'name': 'cvraw',
            'min_salary': 120,
            'max_salary': 200,
            'date_posted': '2021-02-28'
        },
        {
            'name': 'bvraw',
            'min_salary': 110,
            'max_salary': 210,
            'date_posted': '2021-02-27'
        },
        {
            'name': 'avraw',
            'min_salary': 100,
            'max_salary': 220,
            'date_posted': '2021-02-26'
        }
    ]

    criteria = ['min_salary', 'max_salary', 'date_posted']

    # with pytest.raises(ValueError):
    # assert True is True
    # print(sort_by(jobs_group, criteria[0]))
    # print('vraaaawwwwwr')
    for columm in criteria:
        result = sort_by(jobs_group, columm)
        if (columm == 'min_salary'):
            assert result == jobs_group1
        else:
            assert result == jobs_group2
