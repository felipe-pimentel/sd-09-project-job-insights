from functools import lru_cache
from csv import DictReader

@lru_cache
def read(path):
    with open(path, 'r', encoding='utf8') as csvfile:
        content = DictReader(csvfile)
        return [rows for rows in content]
