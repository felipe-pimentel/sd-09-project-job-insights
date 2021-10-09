from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs_dicts = csv.DictReader(file, delimiter=',', quotechar='"')
        jobs_list = [job for job in jobs_dicts]
    return jobs_list
