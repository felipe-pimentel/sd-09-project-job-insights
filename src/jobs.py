from functools import lru_cache
import csv


@lru_cache
def read(path):

    with open(path, mode='r') as csv_file:
        fileContent = csv.DictReader(csv_file)
        return fileContent

# @lru_cache
# def read(path):
#     """Reads a file from a given path and returns its contents

#     Parameters
#     ----------
#     path : str
#         Full path to file

#     Returns
#     -------
#     list
#         List of rows as dicts
#     """
#     with open(path, mode='r') as csv_file:
#         fileContent = csv.DictReader(csv_file)
#         jobs_type = set()
#         for job in fileContent:
#             jobs_type.add(job["job_type"]),

#         print(jobs_type)
#         # return fileContent
