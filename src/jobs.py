from functools import lru_cache
import csv


@lru_cache
def read(path):
    rows = []
    with open(path) as file:
        tableData = list(csv.DictReader(file))
        for row in tableData:
            rows.append(row)
    return rows
