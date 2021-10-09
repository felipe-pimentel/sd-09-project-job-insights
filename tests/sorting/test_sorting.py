from src.sorting import sort_by

mock_jobs = [
    {
        'max_salary': 10000,
        'min_salary': 5000,
        'date_posted': '01-02-2020'
    },
    {
        'max_salary': 5000,
        'min_salary': 2000,
        'date_posted': '04-03-2020'
    },
    {
        'max_salary': 15000,
        'min_salary': 1000,
        'date_posted': '05-03-2020'
    },
    {
        'max_salary': 3000,
        'min_salary': 2500,
        'date_posted': '02-01-2020'
    },
]

right_min_salary = [1000, 2000, 2500, 5000]

right_max_salary = [15000, 10000, 5000, 3000]

right_date_posted = ['05-03-2020', '01-02-2020', '04-03-2020', '02-01-2020']


def test_sort_by_criteria():

    sort_by(mock_jobs, 'min_salary')
    assert [job['min_salary'] for job in mock_jobs] == right_min_salary

    sort_by(mock_jobs, 'max_salary')
    assert [job["max_salary"] for job in mock_jobs] == right_max_salary

    sort_by(mock_jobs, 'date_posted')
    assert [job["date_posted"] for job in mock_jobs] == right_date_posted
