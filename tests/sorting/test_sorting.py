from src.sorting import sort_by
import pytest


@pytest.fixture
def min_salary_mock():
    return [{
        "min_salary": "2000"
    }, {
        "min_salary": "1000"
    }]


def default_salary_mock():
    return [{
        "min_salary": "1000"
    }, {
        "min_salary": "2000"
    }]


def test_sorting_by_criteria(min_salary_mock):
    sort_by(min_salary_mock, "min_salary")
    assert default_salary_mock() == min_salary_mock
