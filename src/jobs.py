from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        file_reader = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = file_reader
    return [data]
