from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        tableFile = csv.DictReader(file, delimiter=',', quotechar='"')
        jobList = []
        for job in tableFile:
            jobList.append(job)
    return jobList
