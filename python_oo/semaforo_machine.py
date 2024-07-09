from transitions import Machine
from time import sleep
from random import randint
from enum import Enum


class States(Enum):
    VERMELHO = 1
    VERDE = 2
    AMARELO = 3
    ERRO = 0


class Semaforo(object):

    def __init__(self) -> None:
        self.cicles = 0
        transitions = [
            {
                'trigger': 'abrir',
                'source': States.VERMELHO,
                'dest': States.VERDE,
            },
            {
                'trigger': 'iniciar_fechar',
                'source': States.VERMELHO,
                'dest': States.VERDE,
            },
            {
                'trigger': 'fechar',
                'source': States.VERMELHO,
                'dest': States.VERDE,
            },
            {
                'trigger': 'fault',
                'source': '*',
                'dest': States.ERRO,
                'conditions': ['fault_state'],
            }
        ]

        self.machine = Machine(
            model=self,
            states=States,
            initial=States.VERMELHO,
            transitions=transitions,
        )

    def abrir(self):
        print(f'Sinal {self.state.name} - Abrindo')
        sleep(3)
        self.cicles += 1

    def iniciar_fechar(self):
        print(f'Sinal {self.state.name} - Amarelando')
        sleep(2)

    def fechar(self):
        print(f'Sinal {self.state.name} - Fechando')
        sleep(3)

    @property
    def fault_state(self):
        return randint(1, 100) <= 2

    def _main_cicle(self):
        while not self.fault_state:
            self.abrir()
            self.iniciar_fechar()
            self.fechar()
            print(self.cicles, 'Ciclos Executados até agora.')
        print('EITA! O SINAL QUEBROU DOIDÃO')
        print(self.cicles, 'Ciclos Executados.')


if __name__ == '__main__':
    s = Semaforo()
    s._main_cicle()
