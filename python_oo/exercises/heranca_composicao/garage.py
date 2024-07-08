from vehicle import Vehicle


class Garage:

    def __init__(
        self,
        spaces: int = 1,
    ) -> None:
        self.__spaces = spaces
        self.__vehicles: list[Vehicle] = []

    def enter(self, vehicle: Vehicle) -> None:
        if not isinstance(vehicle, Vehicle):
            raise SystemError('This garage stores only vehicles.')
        if len(self.__vehicles) < self.__spaces:
            self.__vehicles.append(vehicle)
        raise SystemExit('No space left for another vehicle')

    def exit(self) -> Vehicle:
        if len(self.__vehicles) == 0:
            raise SystemError('No vehicles left at the garage')
        return self.__vehicles.pop()
