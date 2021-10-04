import pytest
from src.sorting import sort_by


def test_sort_by_criteria():

    # criteria_types = ['min_salary', 'max_salary', 'date_posted']

    jobs = [
        {"title": "Front end developer", "salary": "2000", "type": "trainee"},
        {"title": "Back end developer", "salary": "3000", "type": "full time"},
        {
            "title": "Full stack end developer",
            "salary": "4000",
            "type": "full time",
        },
    ]

    # reject unspecified criteria
    with pytest.raises(ValueError):
        sort_by(jobs, "title")
