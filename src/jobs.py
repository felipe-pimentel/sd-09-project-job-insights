from functools import lru_cache
import csv


@lru_cache
def read(path):

    with open(path,  encoding="utf8") as file:
        fileReader = list(csv.DictReader(file))
        return fileReader

    # return [fileReader]


# print(read('jobs.csv'))
