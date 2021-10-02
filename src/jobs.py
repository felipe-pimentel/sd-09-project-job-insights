from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as csv_file:
        file_content = list(csv.DictReader(csv_file))
    return file_content
