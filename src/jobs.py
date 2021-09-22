from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, mode='r') as file:
        table = csv.DictReader(file)
        dict_from_csv = [row for row in table]
        return dict_from_csv
