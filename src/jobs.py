from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, "r") as raw_data:
        data = csv.DictReader(raw_data)
        return [job_info for job_info in data]
