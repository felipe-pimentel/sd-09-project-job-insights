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
        jobs = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs_infos = [job for job in jobs]
        return jobs_infos
