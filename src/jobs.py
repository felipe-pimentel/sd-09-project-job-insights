from functools import lru_cache
from csv import DictReader


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
    with open(path) as csvfile:
        content_read = DictReader(csvfile)
        dict_list = list(content_read)
        return dict_list
