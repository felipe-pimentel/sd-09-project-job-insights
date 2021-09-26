from src.sorting import sort_by


def test_sort_by_criteria():
    jobs =  [
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2021-05-10"},
    {"min_salary": 200, "max_salary": 6000, "date_posted": "2021-05-25"},
    {"min_salary": 3000, "max_salary": 9000, "date_posted": "2021-05-22"},
]

    max_salary = [jobs[0], jobs[1], jobs[2]]
    min_salary = [jobs[1], jobs[0], jobs[2]]
    date_posted = [jobs[0], jobs[2], jobs[1]]

    sort_by(jobs, 'max_salary')
    assert jobs == max_salary

    sort_by(jobs, 'min_salary')
    assert jobs == min_salary

    sort_by(jobs, 'date_posted')
    assert jobs == date_posted