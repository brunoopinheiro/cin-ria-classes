from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, *args, **kwargs):
        pass


class Sujeito:

    LIMIAR = 60

    def __init__(self) -> None:
        self.observers: list[Observer] = []
        self.valor_atual = 0

    def registrar(self, observer: Observer):
        self.observers.append(observer)
        print(f'Observador {observer} adicionado à lista.')

    def desregistrar(self, observer: Observer):
        self.observers.remove(observer)
        print(f'Observador {observer} removido da lista.')

    def mudar_estado(self, valor):
        self.valor_atual = valor
        if valor > Sujeito.LIMIAR:
            self.notify()

    def notify(self):
        for observer in self.observers:
            observer.update(valor=self.valor_atual)


class ConcreteObserver(Observer):
    def __init__(self, nome) -> None:
        self.nome = nome

    def update(self, *args, **kwargs):
        print(f'Observer {self.nome} notificado! {args} {kwargs}')


if __name__ == '__main__':
    print('==== Observer ====')
    sujeito = Sujeito()
    o1 = ConcreteObserver('O1')
    o2 = ConcreteObserver('O2')
    sujeito.registrar(o1)
    sujeito.mudar_estado(40)
    sujeito.mudar_estado(70)
    print()
    sujeito.registrar(o2)
    sujeito.mudar_estado(80)
    print()
    sujeito.desregistrar(o1)
    sujeito.mudar_estado(75)
