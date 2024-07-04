from livro import Livro
from functools import reduce


class Biblioteca:

    def __init__(
        self
    ) -> None:
        self.__colecao: list[Livro] = []

    def adicionar_livro(self, livro: Livro) -> None:
        if not isinstance(livro, Livro):
            raise TypeError('Ainda não suportamos e-book')
        self.__colecao.append(livro)

    def adicionar_colecao(self, lista_livros: list[Livro]) -> None:
        for liv in lista_livros:
            self.adicionar_livro(liv)

    def filtra_num_pgs(self, limit: int) -> list[Livro]:
        return [liv for liv in self.__colecao if liv.paginas >= limit]

    def soma_paginas(self) -> int:
        return reduce(lambda x, y: x+y.paginas, self.__colecao, 0)

    def antes_de(self, ano: int) -> list[Livro]:
        return [liv for liv in self.__colecao if liv.ano < ano]
