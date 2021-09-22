from functools import lru_cache


@lru_cache
def read(path):
    import csv

    with open(path) as file:
        content = list(csv.DictReader(file))
    return content
