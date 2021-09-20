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
    with open(path, newline='') as jobs_file:
        reader = csv.DictReader(jobs_file)
        jobs = []
        for row in reader:
            jobs.append(row)

    return jobs
