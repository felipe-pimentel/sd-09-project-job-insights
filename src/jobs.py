from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobs_infos = csv.reader(path, delimiter=",", quotechar='"')
    return [jobs_infos]


read("jobs.csv")
