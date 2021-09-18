from functools import lru_cache

import csv


@lru_cache
def read(path):

    job_list = []

    with open(path, mode="r") as jobs:
        job_reader = csv.DictReader(jobs, delimiter=",", quotechar='"')

        for job in job_reader:
            job_list.append(job)

    jobs.close

    return job_list
