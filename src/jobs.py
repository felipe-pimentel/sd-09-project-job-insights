from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, mode="r") as file:
        jobs_dictionary = list(csv.DictReader(file))
        return jobs_dictionary
