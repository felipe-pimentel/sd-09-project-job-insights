# import pytest
from src.sorting import sort_by


def assert_iterable(expected, results, criteria):
    for expected_value, resulted_value in zip(expected, results):
        assert expected_value == resulted_value[criteria]


def test_sort_by_criteria():
    keys = ("min_salary", "max_salary", "date_posted")
    values = (
        (1000, 6000, "2021-01-01"),
        (2000, 5000, "2021-01-02"),
        (3000, 4000, "2021-01-03"),
        ("", 3000, "2021-01-04"),
        (5000, "", "2021-01-05"),
        (6000, 1000, ""),
    )
    jobs = [{k: v for k, v in zip(keys, value)} for value in values]

    # Should raise ValueError with invalid criteria keys
    # invalid_criteria_keys = (None, 1 , "", "name")

    # for invalid_criteria_key in invalid_criteria_keys:
    #     with pytest.raises(ValueError):
    #         sort_by(jobs, invalid_criteria_key)

    # Should sort min_salary correctly
    criteria = "min_salary"
    expected = (1000, 2000, 3000, 5000, 6000, "")

    sort_by(jobs, criteria)
    assert_iterable(expected, jobs, criteria)

    # Should sort max_salary correctly
    criteria = "max_salary"
    expected = (6000, 5000, 4000, 3000, 1000, "")

    sort_by(jobs, criteria)
    assert_iterable(expected, jobs, criteria)

    # Should sort date_posted correctly
    criteria = "date_posted"
    expected = (
        "2021-01-05",
        "2021-01-04",
        "2021-01-03",
        "2021-01-02",
        "2021-01-01",
        "",
    )

    sort_by(jobs, criteria)
    assert_iterable(expected, jobs, criteria)
