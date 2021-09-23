from functools import lru_cache


@lru_cache
def read(path):
    import csv
    try:
        with open(path) as file:
            file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            file_list = [job for job in file_reader]
    except OSError:
        print("Arquivo inexistente")
    else:
        return file_list
