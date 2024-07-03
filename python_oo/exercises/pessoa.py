from datetime import date


class Pessoa:
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value) -> None:
        self.__name = value

    @property
    def cpf(self) -> str:
        maskedcpf = f'***{self.__cpf[3:7]}.***-**'
        return maskedcpf

    @property
    def birth_date(self) -> date:
        return self.__birthdate

    @property
    def address(self) -> str:
        return self.__address

    @property
    def formacao(self) -> str:
        return self.__formacao

    @property
    def estado_civil(self) -> str:
        return self.__estadocivil

    def __init__(
            self,
            name: str,
            cpf: str,
            birthdate: date,
            address: str | None = None,
            formacao: str | None = None,
            estado_civil: str | None = None,
            ) -> None:
        self.name = name
        self.__cpf = cpf
        self.__birthdate = birthdate
        self.__address = address
        self.__formacao = formacao
        self.__estadocivil = estado_civil

    def change_address(self, new_address) -> None:
        self.__address = new_address

    def change_formacao(self, formacao) -> None:
        self.__formacao = formacao

    def change_estadocivil(self, estadocivil) -> None:
        self.__estadocivil = estadocivil

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pessoa):
            raise TypeError('Comparação não suportada')
        return self.__cpf == other.__cpf

    def __str__(self) -> str:
        pes = f'Pessoa({self.name}, {self.cpf})'
        return pes


if __name__ == '__main__':
    p1 = Pessoa(
        name='Bruno',
        cpf='123.123.321-12',
        birthdate=date(1993, 6, 24),
        address='Recife',
        estado_civil='Casado',
        formacao='Pós-graduando',
    )
    print(p1)
