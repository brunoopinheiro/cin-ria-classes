from engine import Engine
from tire import Tire
from vehicle import Vehicle


class Motorcycle(Vehicle):

    @property
    def __numtires(self) -> int:
        return 2

    @property
    def has_sidecar(self) -> bool:
        return self.__hassidecar

    def __init__(
        self,
        manufacturer: str,
        model: str,
        engine: Engine,
        tires: list[Tire],
        has_sidecar: bool,
    ) -> None:
        if len(tires) != self.__numtires:
            n = self.__numtires
            raise SystemError(f'WARNING: a motorcyle must have {n} tires')
        super().__init__(manufacturer, model, engine, tires)
        self.__hassidecar = has_sidecar
