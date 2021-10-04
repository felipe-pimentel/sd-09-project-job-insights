from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        file_data = csv.DictReader(file)
        result = []
        for row in file_data:
            result.append(row)
    return result
