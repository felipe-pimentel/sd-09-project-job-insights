from functools import lru_cache
from csv import DictReader


@lru_cache
def read(path):
    with open(path, mode="r", encoding="utf8") as csv_file:
        reader = DictReader(csv_file)
        return [eachjob for eachjob in reader]
