from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, mode="r", encoding="utf8") as file_csv:
        list = csv.DictReader(file_csv)
        return [job for job in list]
