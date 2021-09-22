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
    with open(path) as jobs_file:
        headers, *jobs_list = csv.reader(
            jobs_file,
            delimiter=",",
            quotechar='"'
        )

        all_jobs_list = []
        all_jobs_dict = {}

        for job_list in jobs_list:
            for item in job_list:
                all_jobs_dict[headers[job_list.index(item)]] = item

            all_jobs_list.append(all_jobs_dict.copy())

    return all_jobs_list
