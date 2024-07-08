from vehicle import Vehicle


class ServiceStation:

    @property
    def num(self) -> int:
        return self.__num

    def __init__(
        self,
        num: int,
    ) -> None:
        self.__num = num

    def fix_vehicle(self, vehicle: Vehicle) -> bool:
        if not isinstance(vehicle, Vehicle):
            raise SystemError('This Service Station only supports vehicles')
        model = vehicle.model
        manufacturer = vehicle.manufacturer
        print(f'Vehicle {model} - {manufacturer} was fixed successfully')
        return True
