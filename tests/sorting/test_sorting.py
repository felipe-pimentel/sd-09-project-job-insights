import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "title": 'Full stack end developer',
            "min_salary": '4000',
            "max_salary": '8000'
        }
    ]
    criteria = 'xablau'
    with pytest.raises(ValueError, match='invalid sorting criteria: xablau'):
        sort_by(jobs, criteria)
