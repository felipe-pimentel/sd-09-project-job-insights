from functools import lru_cache


"""
1 - Implemente a função read
local: src/jobs.py

Para começarmos a processar os dados, devemos antes carregá-los em nossa
aplicação. Esta função será responsável por abrir o arquivo CSV e retornar os
dados no formato de uma lista de dicionários.

A função deve receber um path (uma string com o caminho para um arquivo).
A função deve abrir o arquivo e ler seus conteúdos.
A função deve tratar o arquivo como CSV.
A função deve retornar uma lista de dicionários, onde as chaves são os
cabeçalhos de cada coluna e os valores correspondem a cada linha.
writing_hand Teste manual: abra um terminal Python importando estas funções
através do comando python3 -i src/jobs.py e invoque a função utilizando
diferentes paths.

robot O que será verificado pelo avaliador:

A função abre o arquivo passado como parâmetro
A função retorna uma lista de dicionários
A função retorna a quantidade correta de itens na lista
Nos dicionários retornados pela função, as chaves correspondem aos cabeçalhos
do arquivo
"""


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
    return []
