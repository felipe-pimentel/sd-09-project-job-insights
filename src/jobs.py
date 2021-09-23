from functools import lru_cache
import csv


@lru_cache
def read(path: str) -> list:
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
    with open(path, encoding='utf8') as file:
        job_info = csv.DictReader(file, delimiter=',', quotechar='"')
        return [info for info in job_info]
