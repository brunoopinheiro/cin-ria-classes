from vehicle import Vehicle
from service_station import ServiceStation
from random import randint
from time import sleep


class Workshop:

    @property
    def name(self) -> str:
        return self.__name

    def __init__(
        self,
        name: str,
    ) -> None:
        self.__name = name
        self.__stations: dict[int, ServiceStation] = {}
        for i in range(1, 5):
            newstation = ServiceStation(i)
            self.__stations[i] = newstation

    def __str__(self) -> str:
        return f'Workshop: {self.name} {len(self.__stations)} Service Stations'

    def fix_vehicle(self, vehicle: Vehicle, station: int) -> bool:
        if station not in self.__stations:
            print('Invalid Station')
            return False
        print('Maintanance in progress')
        sleep(randint(1, 5))
        return self.__stations[station].fix_vehicle(vehicle)
