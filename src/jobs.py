from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents"""

    with open(path, mode="r") as file:
        reader = csv.DictReader(file)
        retorno = [item for item in reader]
    return retorno


# algumas referencias
# https://www.ti-enxame.com/pt/python/criando-um-dicionario-partir-de-um-arquivo-csv/1069729395/
#  https://www.delftstack.com/pt/howto/python/python-csv-to-dictionary/
#  https://qastack.com.br/programming/6740918/creating-a-dictionary-from-a-csv-file
