from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(f'{path}', 'r') as file:
        read = csv.DictReader(file, delimiter=",")
        for row in read:
            return [row]
