from src.sorting import sort_by


def test_sort_by_criteria():
    jobs_data = [
      {
        "job_name": "Programador",
        "min_salary": "3500",
        "max_salary": "12000",
        "date_posted": "01-10-2021"
      },
      {
        "job_name": "encanador",
        "min_salary": "2000",
        "max_salary": "5000",
        "date_posted": "19-09-2000"
      },
      {
        "job_name": "marceneiro",
        "min_salary": "1200",
        "max_salary": "4000",
        "date_posted": "20-09-2019"
      },
    ]
    min_salary = list((jobs_data))
    # print(min_salary)

    max_salary = list((jobs_data))

    sort_by(jobs_data, "min_salary")
    assert jobs_data == min_salary

    sort_by(jobs_data, "max_salary")
    assert jobs_data == max_salary
