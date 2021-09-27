from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file_csv:
        file_reader = list(
            csv.DictReader(file_csv, delimiter=",", quotechar='"')
        )
    return file_reader
