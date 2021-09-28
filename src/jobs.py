from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, mode='r') as csvfile:
        csv_reader = list(csv.DictReader(
            csvfile, delimiter=",", quotechar='"'))
        return csv_reader
