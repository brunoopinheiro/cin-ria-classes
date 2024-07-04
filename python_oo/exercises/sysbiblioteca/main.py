import os
from livro import Livro
from biblioteca import Biblioteca
from pprint import pprint


def ler_dados(arquivo):
    livros = []
    with open(arquivo, 'r', encoding='utf-8') as f:
        books = f.read().split('\n')
        livros = [b.split(',') for b in books]
    return livros


def main():
    fpath = os.path.join(os.getcwd(), 'biblioteca.txt')
    livros_bruto = ler_dados(fpath)

    biblioteca = Biblioteca()
    livros = [Livro(*liv) for liv in livros_bruto]
    biblioteca.adicionar_colecao(livros)
    print()
    print('Livros com mais de 300 páginas')
    pprint([str(liv) for liv in biblioteca.filtra_num_pgs(300)])
    print()
    print("Total de Páginas: ", biblioteca.soma_paginas())
    print()
    print('Livros Publicados antes de 1950: ')
    pprint([str(liv) for liv in biblioteca.antes_de(1950)])
    print()


if __name__ == '__main__':
    main()
