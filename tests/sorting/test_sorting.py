from src.sorting import sort_by


def test_sort_by_criteria():

    mock_jobs = [
        {
            "min_salary": 2000,
            "max_salary": 6000,
            "date_posted": "2021-01-01"
        },
        {
            "min_salary": 1000,
            "max_salary": 4000,
            "date_posted": "2020-01-01"
        },
        {
            "min_salary": 2500,
            "max_salary": 8000,
            "date_posted": "2015-01-01"
        },
        {
            "min_salary": 5000,
            "max_salary": 16000,
            "date_posted": "2019-01-01"
        }
    ]

    sort_by(mock_jobs, "min_salary")
    assert mock_jobs[0]["min_salary"] == 1000
    assert mock_jobs[1]["min_salary"] == 2000
    assert mock_jobs[2]["min_salary"] == 2500
    assert mock_jobs[3]["min_salary"] == 5000

    sort_by(mock_jobs, "max_salary")
    assert mock_jobs[0]["max_salary"] == 16000
    assert mock_jobs[1]["max_salary"] == 8000
    assert mock_jobs[2]["max_salary"] == 6000
    assert mock_jobs[3]["max_salary"] == 4000

    sort_by(mock_jobs, "date_posted")
    assert mock_jobs[0]["date_posted"] == "2021-01-01"
    assert mock_jobs[1]["date_posted"] == "2020-01-01"
    assert mock_jobs[2]["date_posted"] == "2019-01-01"
    assert mock_jobs[3]["date_posted"] == "2015-01-01"
