from csv import DictReader
from functools import lru_cache


@lru_cache
def read(path):
    job_list = []
    with open(path) as jobs_file:
        for job in DictReader(jobs_file):
            job_list.append(job)

    return job_list
