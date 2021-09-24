# import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "8000",
        },
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "7000",
        },
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "9000",
        },
    ]
    # criteria = "xablau"
    # with pytest.raises(ValueError, match="invalid sorting criteria: xablau"):
    #     sort_by(jobs, criteria)

    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == "9000"
