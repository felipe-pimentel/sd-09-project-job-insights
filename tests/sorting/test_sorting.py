import pytest
from src.sorting import sort_by


@pytest.fixture
def fake_jobs():
    return [
        {'min_salary': 10, 'max_salary': 150, 'date_posted': '2021-09-30'},
        {'min_salary': 20, 'max_salary': 100, 'date_posted': '2021-09-29'},
        {'min_salary': 50, 'max_salary': 200, 'date_posted': '2021-09-28'},
        {'min_salary': 30, 'max_salary': 250, 'date_posted': '2021-09-27'},
    ]


def jobs_sorted_by_min_salary():
    return [
        {'min_salary': 10, 'max_salary': 150, 'date_posted': '2021-09-30'},
        {'min_salary': 20, 'max_salary': 100, 'date_posted': '2021-09-29'},
        {'min_salary': 30, 'max_salary': 250, 'date_posted': '2021-09-27'},
        {'min_salary': 50, 'max_salary': 200, 'date_posted': '2021-09-28'},
    ]


def jobs_sorted_by_max_salary():
    return [
        {'min_salary': 30, 'max_salary': 250, 'date_posted': '2021-09-27'},
        {'min_salary': 50, 'max_salary': 200, 'date_posted': '2021-09-28'},
        {'min_salary': 10, 'max_salary': 150, 'date_posted': '2021-09-30'},
        {'min_salary': 20, 'max_salary': 100, 'date_posted': '2021-09-29'},
    ]


def jobs_sorted_by_date_posted():
    return [
        {'min_salary': 10, 'max_salary': 150, 'date_posted': '2021-09-30'},
        {'min_salary': 20, 'max_salary': 100, 'date_posted': '2021-09-29'},
        {'min_salary': 50, 'max_salary': 200, 'date_posted': '2021-09-28'},
        {'min_salary': 30, 'max_salary': 250, 'date_posted': '2021-09-27'},
    ]


def test_sort_by_criteria(fake_jobs):
    sort_by(fake_jobs, 'min_salary')
    assert fake_jobs == jobs_sorted_by_min_salary()
    sort_by(fake_jobs, 'max_salary')
    assert fake_jobs == jobs_sorted_by_max_salary()
    sort_by(fake_jobs, 'date_posted')
    assert fake_jobs == jobs_sorted_by_date_posted()
