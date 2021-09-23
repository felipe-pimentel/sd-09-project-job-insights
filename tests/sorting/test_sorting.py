from src.sorting import sort_by

employee_1 = {
    "min_salary": 10,
    "max_salary": 100,
    "date_posted": "2021-09-23"}

employee_2 = {
    "min_salary": 100,
    "max_salary": 1000,
    "date_posted": "2021-09-24",
}

employee_3 = {
    "min_salary": 1000,
    "max_salary": 10000,
    "date_posted": "2021-09-25",
}

employee_4 = {
    "min_salary": 10000,
    "max_salary": 100000,
    "date_posted": "2021-10-26",
}

jobs = [
    employee_1,
    employee_2,
    employee_3,
    employee_4,
]

expected = [
    [employee_1, employee_2, employee_3, employee_4],
    [employee_4, employee_3, employee_2, employee_1],
    [employee_4, employee_3, employee_2, employee_1],
]


def test_sort_by_criteria():
    criteria = ["min_salary", "max_salary", "date_posted"]
    for index in range(len(criteria)):
        sort_by(jobs, criteria[index])

        assert jobs == expected[index]
