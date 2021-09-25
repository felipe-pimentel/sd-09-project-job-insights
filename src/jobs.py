import csv
from functools import lru_cache


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
    with open(path) as file:
        file_csv = csv.DictReader(file)
        list_jobs = []

        for line in file_csv:
            list_jobs.append(line)

    return list_jobs
