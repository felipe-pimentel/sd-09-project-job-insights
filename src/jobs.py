from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        job_list = list(csv.DictReader(file, delimiter=",", quotechar='"'))
    return job_list
