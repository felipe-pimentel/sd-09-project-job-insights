import csv
from functools import lru_cache


@lru_cache(maxsize=None)
def read(path):
    try:
        with open(path) as file:
            job_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            job_reader = [dict(job) for job in job_reader]
            return job_reader
    except OSError:
        return("Não foi possível ler o arquivo")
    finally:
        print("Tentativa de ler o arquivo")


# print(read("src/jobs.csv"))


# for result in read("src/jobs.csv"):
#   print(type(result))
# print(type(read("src/jobs.csv")))
# print(len(read("src/jobs.csv")))
