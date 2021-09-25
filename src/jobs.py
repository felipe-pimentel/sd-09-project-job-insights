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
    jobs = []
    with open(path) as jobs_file:
        reader = csv.DictReader(jobs_file)
        for line in reader:
            jobs.append(line)

    return jobs


# print(read("tests/mocks/jobs.csv"))
