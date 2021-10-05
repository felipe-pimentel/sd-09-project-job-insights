from functools import lru_cache
import csv


@lru_cache
def read(path):
    data = []
    with open(path) as file:
        content = csv.DictReader(file, delimiter=',', quotechar='"')
        for row in content:
            data.append(row)
    return data
