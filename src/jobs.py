from functools import lru_cache
import csv


@lru_cache
def read(path):

    with open("jobs.csv", "w") as file:
        header_table = csv.reader(file, delimiter=",", quotechar='"')
        header, *table = header_table

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
    return [table]
