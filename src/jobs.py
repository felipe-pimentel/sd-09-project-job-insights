from functools import lru_cache


@lru_cache
def read(path):
    import csv

    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file
    """
    with open(path) as file:
        file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        file_list = [job for job in file_reader]
    """"
    Returns
    -------
    list
        List of rows as dicts
    """
    return file_list
