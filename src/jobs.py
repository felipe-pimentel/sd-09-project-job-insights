from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as f:
        csv_reader = csv.DictReader(f)
        csv_list = list(csv_reader)
        return csv_list
