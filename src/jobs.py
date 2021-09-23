import csv
from functools import lru_cache


@lru_cache
def read(path):
    result = []
    with open(path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for row in jobs_reader:
            result.append(row)

    return result


# print(read("src/jobs.csv"))

# def test_sort_by_criteria():
#     jobs = read("tests/mocks/jobs_with_salaries_and_date.csv")
#     print(jobs)


# test_sort_by_criteria()
