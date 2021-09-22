from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, mode='r') as file:
        table = csv.reader(file)
        dict_from_csv = {rows[0]: rows[1] for rows in table}
        return dict_from_csv
