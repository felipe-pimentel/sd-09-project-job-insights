from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        header_table = csv.DictReader(file)
        list_of_rows = [row for row in header_table]
        return list_of_rows

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
