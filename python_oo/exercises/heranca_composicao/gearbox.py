class Gearbox:

    @property
    def gear(self) -> int:
        return self.__gear

    def __init__(
        self,
    ) -> None:
        self.__gear = 0

    def update_gear(self, acceleration) -> None:
        if acceleration < 0:
            self.__gear = -1
        if acceleration == 0:
            self.__gear = 0
        if acceleration >= 1 and acceleration <= 25:
            self.__gear = 1
        if acceleration > 25 and acceleration <= 50:
            self.__gear = 2
        if acceleration > 50 and acceleration <= 100:
            self.__gear = 3
        if acceleration > 100 and acceleration <= 150:
            self.__gear = 4
        if acceleration > 150 and acceleration <= 200:
            self.__gear = 5
