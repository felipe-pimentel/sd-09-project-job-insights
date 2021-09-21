from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        read_jobs = csv.DictReader(file)
        jobs = []
        for job in read_jobs:
            jobs.append(job)
    return jobs
