from src.sorting import sort_by
import pytest


job_1 = {'date_posted': '2001-05-05', 'max_salary': 3000, 'min_salary': 1000}
job_2 = {'date_posted': '2010-06-01', 'max_salary': 12000, 'min_salary': 5000}
job_3 = {'date_posted': '2020-02-30', 'max_salary': 9000, 'min_salary': 2000}

allJobs = [job_1, job_2, job_3]
sorted_by_date = [job_3, job_2, job_1]
sorted_by_max = [job_2, job_3, job_1]
sorted_by_min = [job_1, job_3, job_2]


def test_sort_by_criteria():
    sort_by(allJobs, 'date_posted')
    assert sorted_by_date == allJobs

    sort_by(allJobs, 'max_salary')
    assert sorted_by_max == allJobs

    sort_by(allJobs, 'min_salary')
    assert sorted_by_min == allJobs

    with pytest.raises(ValueError):
        sort_by(allJobs, 'xerif')
