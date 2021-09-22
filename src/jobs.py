from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        table = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs = []
        for job in table:
            jobs.append(job)
        return jobs
