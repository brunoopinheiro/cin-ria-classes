from abc import ABC, abstractmethod
from enum import Enum
from math import pi


class FormaGeometrica(ABC):

    @property
    @abstractmethod
    def area(self) -> float:
        raise NotImplementedError

    @property
    @abstractmethod
    def perimetro(self) -> float:
        raise NotImplementedError

    @property
    @abstractmethod
    def nome_forma(self) -> str:
        raise NotADirectoryError


class Circulo(FormaGeometrica):

    def __init__(self, raio: float) -> None:
        self.raio = raio

    @property
    def area(self) -> float:
        return pi * (self.raio ** 2)

    @property
    def perimetro(self) -> float:
        return 2 * pi * self.raio

    @property
    def nome_forma(self) -> str:
        return 'Circulo'


class Quadrado(FormaGeometrica):

    def __init__(self, lado: float) -> None:
        self.lado = lado

    @property
    def area(self) -> float:
        return self.lado ** 2

    @property
    def perimetro(self) -> float:
        return self.lado * 4

    @property
    def nome_forma(self) -> str:
        return 'Quadrado'


class Formas(Enum):
    Circulo = 1
    Quadrado = 2


class FormaFactory:

    @staticmethod
    def criar_forma(tipo_forma: Formas, *args, **kwargs) -> FormaGeometrica:
        if tipo_forma == Formas.Circulo:
            return Circulo(*args, **kwargs)
        elif tipo_forma == Formas.Quadrado:
            return Quadrado(*args, **kwargs)
        else:
            raise TypeError('Unsuported Type or Wrong Arguments')


if __name__ == '__main__':
    circulo = FormaFactory.criar_forma(
        tipo_forma=Formas.Circulo,
        raio=2.0,
    )
    quadrado = FormaFactory.criar_forma(
        tipo_forma=Formas.Quadrado,
        lado=4.0,
    )
    for shape in [circulo, quadrado]:
        msg = f'{shape.nome_forma} (Área: {shape.area} Per: {shape.perimetro})'
        print(msg)
