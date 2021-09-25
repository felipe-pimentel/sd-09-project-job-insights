from functools import lru_cache
import csv


@lru_cache
def read(path):
    initial_list = []
    with open(path, mode='r') as jobs_file:
        jobs_list = csv.DictReader(jobs_file)
        for job in jobs_list:
            initial_list.append(job)
    return initial_list
