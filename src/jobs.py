import csv
from functools import lru_cache
from os import path


@lru_cache
def read(path):
    with open(path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        print('test')
        jobs_data = []
        for row in jobs_reader:
            jobs_data.append(row)

        return jobs_data
