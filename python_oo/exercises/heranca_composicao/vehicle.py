from abc import ABC
from engine import Engine
from tire import Tire


class Vehicle(ABC):

    @property
    def manufacturer(self) -> str:
        return self.__manufacturer

    @property
    def model(self) -> str:
        return self.__model

    @property
    def current_speed(self) -> int:
        return self.__engine.acceleration

    @property
    def current_gear(self) -> int:
        return self.__engine.gear

    def __init__(
        self,
        manufacturer: str,
        model: str,
        engine: Engine,
        tires: list[Tire],
    ) -> None:
        self.__manufacturer = manufacturer
        self.__model = model
        self.__engine = engine
        self.__tires = tires

    def turn_on(self) -> None:
        self.__engine.turn_on()

    def turn_off(self) -> None:
        self.__engine.turn_off()

    def __updaterotations(self) -> None:
        tiresize = self.__tires[0].size
        rt = (self.__engine.strength * self.__engine.gear) * 200 / tiresize
        rotation = round(rt)
        for t in self.__tires:
            t.rotations = rotation

    def speed_up(self) -> None:
        if self.__engine.state:
            self.__engine.speed_up()
            self.__updaterotations()

    def speed_down(self) -> None:
        if self.__engine.state:
            self.__engine.speed_down()
            self.__updaterotations()
