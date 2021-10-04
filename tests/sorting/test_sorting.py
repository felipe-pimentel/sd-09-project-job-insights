import pytest
from src.sorting import sort_by


@pytest.fixture
def sorting_by_criteria():
    return [
        {"max_salary": 726, "min_salary": 0, "date_posted": "2011-01-01"},
        {"max_salary": 479, "min_salary": 23, "date_posted": "2014-02-28"},
        {"max_salary": 15848, "min_salary": 546, "date_posted": "2018-12-17"},
        {"max_salary": 15000, "min_salary": 5, "date_posted": "2012-08-04"},
        {"max_salary": 8723, "min_salary": 1, "date_posted": "2020-01-13"},
        {"max_salary": 33682, "min_salary": 2639, "date_posted": "2011-02-16"},
    ]


def test_sort_by_criteria(sorting_by_criteria):
    sort_types = ["min_salary", "max_salary", "date_posted"]

    for type in sort_types:
        result = sort_by(sorting_by_criteria, type)

        if type == "min_salary":
            assert result[0]["min_salary"] == 0
            assert result[1]["min_salary"] == 1
            assert result[2]["min_salary"] == 5
            assert result[3]["min_salary"] == 23
            assert result[4]["min_salary"] == 546
            assert result[5]["min_salary"] == 2639
        elif type == "max_salary":
            assert result[0]["max_salary"] == 33682
            assert result[1]["max_salary"] == 15848
            assert result[2]["max_salary"] == 15000
            assert result[3]["max_salary"] == 8723
            assert result[4]["max_salary"] == 726
            assert result[5]["max_salary"] == 479
        else:
            assert result[0]["date_posted"] == "2020-01-13"
            assert result[1]["date_posted"] == "2018-12-17"
            assert result[2]["date_posted"] == "2014-02-28"
            assert result[3]["date_posted"] == "2012-08-04"
            assert result[4]["date_posted"] == "2011-02-16"
            assert result[5]["date_posted"] == "2011-01-01"
