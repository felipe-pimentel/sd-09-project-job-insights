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
        results = [line for line in file_csv]

        # for line in file_csv:
        #     results.append(line)

    return results
