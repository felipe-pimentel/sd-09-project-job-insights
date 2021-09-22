import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, "r") as file:
        jobs_reader = csv.reader(file, delimiter=",")
        headers, *data = jobs_reader

    result = []
    for row in data:
        list = {}
        for index in range(len(headers)):
            key = headers[index]
            value = row[index]
            list[key] = value
        result.append(list)

    return result
