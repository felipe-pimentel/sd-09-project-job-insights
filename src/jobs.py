from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        dictResult = csv.DictReader(file, delimiter=",", quotechar='"')
        return [row for row in dictResult]
