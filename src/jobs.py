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

    with open(path, mode="r") as file:
        jobs_list = csv.DictReader(file)
        lista = []
        for value in jobs_list:
            lista.append(value)
        return lista
        # return [value for value in jobs_list]


# jobs_list[1:3]

# print(len(read("./jobs.csv")))
