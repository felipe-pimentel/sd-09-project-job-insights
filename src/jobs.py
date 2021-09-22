import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as jobs_stream:
        return list(csv.DictReader(jobs_stream, delimiter=","))
