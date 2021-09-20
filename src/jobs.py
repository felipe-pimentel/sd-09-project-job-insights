from functools import lru_cache
from csv import DictReader


@lru_cache
def read(path):
    with open(path, mode="r", encoding="utf8") as csvFile:
        reader = DictReader(csvFile)
        return [row for row in reader]
