from functools import lru_cache
from csv import DictReader

@lru_cache
def read(path):

    with open(path) as file:
        return list(DictReader(file))

