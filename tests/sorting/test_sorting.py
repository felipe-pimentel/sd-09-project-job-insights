import pytest
from src.sorting import sort_by


def assert_iterable(expected, results):
    for expected_value, resulted_value in zip(expected, results):
        assert expected_value == resulted_value


def test_sort_by_criteria():
    keys = ("min_salary", "max_salary", "date_posted")
    values = (
        (1, 6, "2021-01-01"),
        (2, 5, "2021-01-02"),
        (3, 4, "2021-01-03"),
        ("", 3, "2021-01-04"),
        (5, "", "2021-01-05"),
        (6, 1, ""),
    )
    jobs = [{k: v for k, v in zip(keys, value)} for value in values]

    # Should raise ValueError with invalid criteria keys
    invalid_criteria_keys = ["name"]

    for invalid_criteria_key in invalid_criteria_keys:
        with pytest.raises(ValueError):
            sort_by(jobs, invalid_criteria_key)

    # Should sort min_salary correctly
    criteria = "min_salary"
    expected = (
        jobs[0],
        jobs[1],
        jobs[2],
        jobs[4],
        jobs[5],
        jobs[3],
    )
    results = sort_by(jobs, criteria)
    print(criteria, results)

    for expected_value, resulted_value in zip(expected, results):
        assert expected_value == resulted_value

    # Should sort max_salary correctly
    criteria = "max_salary"
    expected = (
        jobs[0],
        jobs[1],
        jobs[2],
        jobs[3],
        jobs[5],
        jobs[4],
    )
    results = sort_by(jobs, criteria)
    print(criteria, results)

    for expected_value, resulted_value in zip(expected, results):
        assert expected_value == resulted_value

    # Should sort date_posted correctly
    criteria = "date_posted"
    expected = (
        jobs[0],
        jobs[1],
        jobs[2],
        jobs[3],
        jobs[4],
        jobs[5],
    )
    print(sort_by)
    results = sort_by(jobs, criteria)
    print(criteria, results)
    for expected_value, resulted_value in zip(expected, results):
        assert expected_value == resulted_value
