from src.sorting import sort_by
import pytest


JOB_1 = {
    "min_salary": 35000,
    "max_salary": 45000,
    "date_posted": "2020-10-01",
}

JOB_2 = {
    "min_salary": 19000,
    "max_salary": 28000,
    "date_posted": "2020-09-01",
}

JOB_3 = {
    "min_salary": 10000,
    "max_salary": 15000,
    "date_posted": "2020-03-01",
}

JOB_4 = {
    "min_salary": 50000,
    "max_salary": 55000,
    "date_posted": "2020-05-01",
}

JOB_5 = {
    "min_salary": 21000,
    "max_salary": 24000,
    "date_posted": "2021-01-01",
}

MIN_SALARY_SORT = [JOB_3, JOB_2, JOB_5, JOB_1, JOB_4]
MAX_SALARY_SORT = [JOB_4, JOB_1, JOB_2, JOB_5, JOB_3]
DATE_SORT = [JOB_5, JOB_1, JOB_2, JOB_4, JOB_3]
EXPECTED = {
    "min_salary": MIN_SALARY_SORT,
    "max_salary": MAX_SALARY_SORT,
    "date_posted": DATE_SORT,
}
CRITERIA_OPTIONS = ["min_salary", "max_salary", "date_posted"]

jobs_list = [JOB_1, JOB_2, JOB_3, JOB_4, JOB_5]


def test_sort_by_criteria():
    for option in range(len(CRITERIA_OPTIONS)):
        sort_by(jobs_list, CRITERIA_OPTIONS[option])
        assert jobs_list == EXPECTED[CRITERIA_OPTIONS[option]]
    with pytest.raises(ValueError):
        sort_by(jobs_list, "thiscriterydontexists")
