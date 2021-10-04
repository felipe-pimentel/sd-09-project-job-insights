from src.sorting import sort_by


def test_sort_by_criteria():
    first_listed_jobs = [
        {
            "name": "bla_job",
            "min_salary": 3600,
            "max_salary": 5700,
            "date_posted": "2020-08-12"
        },
        {
            "name": "ble_job",
            "min_salary": 1800,
            "max_salary": 2500,
            "date_posted": "2019-01-01"
        },
        {
            "name": "bli_job",
            "min_salary": 2800,
            "max_salary": 4300,
            "date_posted": "2018-05-18"
        }
    ]

    second_listed_jobs = [
        {
            "name": "blabla_job",
            "min_salary": 1400,
            "max_salary": 3100,
            "date_posted": "2017-06-23"
        },
        {
            "name": "bleble_job",
            "min_salary": 2400,
            "max_salary": 3900,
            "date_posted": "2015-03-20"
        },
        {
            "name": "blibli_job",
            "min_salary": 4100,
            "max_salary": 6800,
            "date_posted": "2021-09-30"
        }
    ]

    third_listed_jobs = [
        {
            "name": "blablabla_job",
            "min_salary": 7800,
            "max_salary": 9600,
            "date_posted": "2014-02-06"
        },
        {
            "name": "blebleble_job",
            "min_salary": 5400,
            "max_salary": 7300,
            "date_posted": "2021-04-11"
        },
        {
            "name": "bliblibli_job",
            "min_salary": 2250,
            "max_salary": 4350,
            "date_posted": "2014-12-16"
        }
    ]

    sort_criteria = ["min_salary", "max_salary", "date_posted"]

    for eachcriteria in sort_criteria:
        result = sort_by(first_listed_jobs, eachcriteria)
        if (eachcriteria == "min_salary"):
            assert result == second_listed_jobs
        else:
            assert result == third_listed_jobs
