from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        dictResult = csv.DictReader(file, delimiter=",", quotechar='"')
        return [row for row in dictResult]
        

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
