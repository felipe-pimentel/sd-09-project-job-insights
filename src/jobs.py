from functools import lru_cache

import csv


@lru_cache
def read(path):
    result_list = []

    with open(path) as filejobs:
        content = csv.DictReader(filejobs, delimiter=",")
        for row in content:
            result_list.append(row)
    
    return result_list
