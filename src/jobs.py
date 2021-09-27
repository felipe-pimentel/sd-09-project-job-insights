from functools import lru_cache
import csv

@lru_cache
def read(path):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        header, *data = csv_reader

        job_list = []
        for job in data:
            job_row = {}
            for index in range(len(header)):
                job_row[header[index]] = job[index]
            job_list.append(job_row)

    return job_list
