from src.sorting import sort_by


def test_sort_by_criteria():
    """
    It tests the sort_by function

    Parameters
    ----------
    jobs : list
        List of dicts representing the jobs.
    criteria : str
        One of `min_salary`, `max_salary` or `date_posted`.
    """

    JOBS = [
        {'max_salary': 15432, 'min_salary': 2000, 'date_posted': '2021-04-12'},
        {'max_salary': None, 'min_salary': 2000, 'date_posted': '2021-04-12'},
        {'max_salary': 16323, 'min_salary': 1000, 'date_posted': '2021-12-07'},
        {'max_salary': 11435, 'min_salary': 4000, 'date_posted': '2021-11-29'},
    ]

    EXPECTED_RESULT_MIN_SALARY = [
        {'max_salary': 16323, 'min_salary': 1000, 'date_posted': '2021-12-07'},
        {'max_salary': 15432, 'min_salary': 2000, 'date_posted': '2021-04-12'},
        {'max_salary': 11435, 'min_salary': 4000, 'date_posted': '2021-11-29'},
        {'max_salary': 15432, 'min_salary': None, 'date_posted': '2021-04-12'},
    ]

    EXPECTED_RESULT_MAX_SALARY = [
        {'max_salary': 16323, 'min_salary': 1000, 'date_posted': '2021-12-07'},
        {'max_salary': 15432, 'min_salary': 2000, 'date_posted': '2021-04-12'},
        {'max_salary': 11435, 'min_salary': 4000, 'date_posted': '2021-11-29'},
        {'max_salary': None, 'min_salary': 2000, 'date_posted': '2021-04-12'},
    ]

    EXPECTED_RESULT_DATE_POSTED = [
        {'max_salary': 16323, 'min_salary': 1000, 'date_posted': '2021-12-07'},
        {'max_salary': 11435, 'min_salary': 4000, 'date_posted': '2021-11-29'},
        {'max_salary': 15432, 'min_salary': 2000, 'date_posted': '2021-04-12'},
        {'max_salary': 15432, 'min_salary': 2000, 'date_posted': None},
    ]

    sort_by(JOBS, 'min_salary')
    assert(JOBS == EXPECTED_RESULT_MIN_SALARY)

    sort_by(JOBS, 'max_salary')
    assert(JOBS == EXPECTED_RESULT_MAX_SALARY)

    sort_by(JOBS, 'date_posted')
    assert(JOBS == EXPECTED_RESULT_DATE_POSTED)
