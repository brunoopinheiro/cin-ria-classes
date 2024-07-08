from engine import Engine
from tire import Tire
from vehicle import Vehicle


class Car(Vehicle):

    @property
    def __numtires(self) -> int:
        return 4

    @property
    def num_doors(self) -> int:
        return self.__numdoors

    def __init__(
        self,
        manufacturer: str,
        model: str,
        engine: Engine,
        tires: list[Tire],
        num_doors: int,
    ) -> None:
        if len(tires) != self.__numtires:
            n = self.__numtires
            raise SystemError(f'WARNING: A car must have {n} tires')
        super().__init__(manufacturer, model, engine, tires)
        self.__numdoors = num_doors
