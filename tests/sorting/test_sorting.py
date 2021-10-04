import pytest
from src.sorting import sort_by


@pytest.fixture
def sorting_by_criteria():
    return [
        {"max_salary": 726, "min_salary": 2, "date_posted": "2011-01-01"},
        {"max_salary": 479, "min_salary": 23, "date_posted": "2014-02-28"},
        {"max_salary": 15848, "min_salary": 546, "date_posted": "2018-12-17"},
        {"max_salary": 15000, "min_salary": 5, "date_posted": "2012-08-04"},
        {"max_salary": 8723, "min_salary": 1, "date_posted": "2020-01-13"},
        {"max_salary": 33682, "min_salary": 2639, "date_posted": "2011-02-16"},
        {"max_salary": None, "min_salary": None, "date_posted": None},
    ]


def test_sort_by_criteria(sorting_by_criteria):
    sort_types = ['max_salary', 'min_salary', 'date_posted']
    expect_min_salary = [1, 2, 5, 23, 546, 2639]
    expect_max_salary = [33682, 15848, 15000, 8723, 726, 479]
    expect_date_posted = [
        "2020-01-13",
        "2018-12-17",
        "2014-02-28",
        "2012-08-04",
        "2011-02-16",
        "2011-01-01",
    ]

    for type in sort_types:
        list_sorting = sort_by(sorting_by_criteria, type)

        if list_sorting is None:
            assert list_sorting is None
        else:
            list_sorting = [job[type] for job in list_sorting]

            if type == "min_salary":
                assert list_sorting == expect_min_salary
            elif type == "max_salary":
                assert list_sorting == expect_max_salary
            else:
                assert list_sorting == expect_date_posted
