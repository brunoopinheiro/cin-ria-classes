class Livro:

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def autor(self) -> str:
        return self.__autor

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, _ano: int) -> None:
        _ano = int(_ano)
        if _ano < 0:
            raise ValueError('Ano Inválido')
        self.__ano = _ano

    @property
    def paginas(self) -> int:
        return int(self.__paginas)

    @paginas.setter
    def paginas(self, _paginas: int) -> None:
        _paginas = int(_paginas)
        if _paginas < 0:
            raise ValueError('Número de Páginas inválido')
        self.__paginas = _paginas

    def __init__(
        self,
        titulo: str,
        autor: str,
        ano: int,
        paginas: int,
    ) -> None:
        self.__titulo = titulo
        self.__autor = autor
        self.ano = ano
        self.__paginas = paginas

    def __str__(self) -> str:
        return f'{self.titulo}, {self.autor} ({self.ano}) - {self.paginas} pgs'
