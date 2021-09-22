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
    all_jobs = []

    with open(path) as file:
        data = csv.DictReader(file, delimiter=",", quotechar='"')
        for info_job in data:
            all_jobs.append(info_job)

    return all_jobs
