from functools import lru_cache
import csv


@lru_cache
def read(path):
    response = []
    with open(path) as file:
        file_reader = csv.reader(file, delimiter=",", quotechar='"')
        header, *row_data = file_reader
        for item in row_data:
            new_dict = {}
            for index, h_item in enumerate(header):
                new_dict[h_item] = item[index]
            response.append(new_dict)
    return response
