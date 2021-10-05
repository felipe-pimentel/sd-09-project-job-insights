from functools import lru_cache
import csv


@lru_cache
def read(path):
    res = []
    with open(path, "r") as file:
        readerFile = csv.DictReader(file)
        for row in readerFile:
            res.append(row)
    return res
