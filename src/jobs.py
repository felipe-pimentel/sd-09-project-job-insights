import csv
from functools import lru_cache


@lru_cache(maxsize=None)
def read(path):

    with open(path) as file:
        jobs_reader = csv.DictReader(file)
        jobs = [job for job in jobs_reader]

        new_list = []

        for job in jobs:
            new_list.append(dict(job))
       
    return new_list
