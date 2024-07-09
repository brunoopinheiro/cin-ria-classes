from enum import Enum


class Estado(Enum):
    TESTE = 1
    VERMELHO = 2
    AMARELO = 3
    VERDE = 4
    ERRO = 5


class Semaforo:
    def __init__(self) -> None:
        self.estado = Estado.TESTE

    def __str__(self) -> str:
        return f'Semáforo: {self.estado.name}'

    def trocar(self):
        if self.estado == Estado.TESTE:
            self.estado = Estado.VERMELHO
        elif self.estado == Estado.VERMELHO:
            self.estado = Estado.VERDE
        elif self.estado == Estado.VERDE:
            self.estado = Estado.AMARELO
        elif self.estado == Estado.AMARELO:
            self.estado = Estado.VERMELHO
        else:
            self.estado = Estado.ERRO

    def erro(self):
        self.estado = Estado.ERRO


if __name__ == "__main__":
    sem = Semaforo()
    print(sem)
    for _ in range(7):
        print(sem)
        sem.trocar()
        print(sem)
        print()

    sem.erro()
    print(sem)
    sem.trocar()
    print(sem)
