from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as csv_file:
        reader_csv = csv.reader(csv_file)
        header, *jobs = reader_csv

        job_list = []

        for job in jobs:
            job_row = {}

            for index in range(len(header)):
                job_row[header[index]] = job[index]
            job_list.append(job_row)
    return job_list
