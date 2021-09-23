from src.sorting import sort_by
import pytest


@pytest.fixture
def min_salary_mock():
    return [{
        "min_salary": "2000"
    }, {
        "min_salary": "1000"
    }]


@pytest.fixture
def max_salary_mock():
    return [{
        "min_salary": "2000"
    }, {
        "min_salary": "1000"
    }]


def min_salary_assert():
    return [{
        "min_salary": "1000"
    }, {
        "min_salary": "2000"
    }]


def max_salary_assert():
    return [{
        "min_salary": "2000"
    }, {
        "min_salary": "1000"
    }]


def test_sorting_by_criteria(min_salary_mock, max_salary_mock):
    sort_by(min_salary_mock, "min_salary")
    assert min_salary_assert() == min_salary_mock

    sort_by(max_salary_mock, "max_salary")
    assert max_salary_assert() == max_salary_mock
