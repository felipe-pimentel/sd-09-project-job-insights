from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs_list = list(csv.DictReader(file))
        return jobs_list
