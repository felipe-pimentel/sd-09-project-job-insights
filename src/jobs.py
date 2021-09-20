from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents
    """
    with open(path, mode='r') as file:
        file_reader = csv.DictReader(file, delimiter=",")
        return [row for row in file_reader]
    """
    Parameters
    ----------
    path : str
        Full path to file
    """

    """
    Returns
    -------
    list
        List of rows as dicts
    """
