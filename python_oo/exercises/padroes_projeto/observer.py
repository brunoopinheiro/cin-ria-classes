from abc import ABC, abstractmethod


class Observer(ABC):

    @property
    def observer_id(self) -> int:
        return self.__observerid

    @observer_id.setter
    def observer_id(self, value) -> None:
        if self.__observerid is None:
            self.__observerid = value

    def __init__(self) -> None:
        self.__observerid = None

    @abstractmethod
    def update(self, *args, **kwargs):
        raise NotImplementedError

    def register(self, observer_id: int) -> None:
        self.observer_id = observer_id


class Tela(Observer):

    def update(self, *args, **kwargs):
        print(f'MOSTRANDO: {args} {kwargs}')


class Subscriber:

    def __init__(self) -> None:
        self.__observers: dict[int, dict] = {}
        self.__lastid = 0

    def register(self, observer: Observer) -> None:
        if not isinstance(observer, Observer):
            raise TypeError('This is not a valid observer')
        if observer.observer_id is not None:
            self.__observers[observer.observer_id]['registered'] = True
        nextid = self.__lastid + 1
        self.__observers[nextid] = {
            'observer': observer,
            'registered': True
        }
        observer.register(nextid)
        self.__lastid = nextid

    def unregister(self, observerid: int) -> None:
        if observerid in self.__observers:
            self.__observers[observerid]['registered'] = False

    def __notify(self, *args, **kwargs):
        for observer in self.__observers.values():
            if observer['registered'] is True:
                observer['observer'].update(*args, **kwargs)

    def trigger_notification(self, *args, **kwargs):
        self.__notify(*args, **kwargs)


if __name__ == '__main__':
    tela = Tela()
    feed = Subscriber()

    feed.register(tela)
    print(tela.observer_id)

    print()
    print('Notifying to the observers')
    feed.trigger_notification(
        action='CHANGE_CHANNEL',
        channel=42,
    )
    feed.unregister(tela.observer_id)

    print('Notify to no one.')
    feed.trigger_notification(
        action='TO_NO_ONE',
    )
