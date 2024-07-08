from gearbox import Gearbox


class Engine:

    @property
    def strength(self) -> int:
        return self.__potency * self.acceleration

    @property
    def acceleration(self) -> int:
        return self.__acceleration

    @property
    def state(self) -> bool:
        return self.__on

    @property
    def gear(self) -> int:
        return self.__gearbox.gear

    def __init__(
        self,
        potency: int,
    ) -> None:
        self.__potency = potency
        self.__acceleration = 0
        self.__on = False
        self.__gearbox = Gearbox()
        self.__increment = 25

    def turn_on(self) -> None:
        if self.__on:
            raise SystemError('WARNING: The car was already on')
        self.__on = True

    def turn_off(self) -> None:
        if self.__on is False:
            raise SystemError('WARNING: Tha car was already off')
        self.__on = False

    def speed_up(self) -> None:
        if self.__on is False:
            raise SystemError('WARNING: Engine is off')
        if self.acceleration >= 200:
            raise SystemError('WARNING: Maximum speed')
        self.__acceleration += self.__increment
        self.__gearbox.update_gear(self.__acceleration)

    def speed_down(self) -> None:
        if self.__on is False:
            raise SystemError('WARNING: Engine is off')
        if self.__acceleration <= -50:
            raise SystemError('WARNING: Maximum reverse speed')
        self.__acceleration -= self.__increment
        self.__gearbox.update_gear(self.__acceleration)
