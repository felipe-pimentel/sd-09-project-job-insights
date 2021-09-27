from functools import lru_cache
import csv


@lru_cache
def read(path):

    with open(path, mode='r') as csv_file:
        fileContent = csv.DictReader(csv_file)
        return fileContent

# @lru_cache
# def read(path):
#     with open(path, mode='r') as csv_file:
#         fileContent = csv.DictReader(csv_file)
#         industries_types = set()
#         for job in fileContent:
#             if job['industry'] != "":
#                 industries_types.add(job["industry"]),
#         industries_types_array = [*industries_types]
#         print(industries_types_array)
#         print(len(industries_types_array))
#         # return fileContent


# read('jobs.csv')
