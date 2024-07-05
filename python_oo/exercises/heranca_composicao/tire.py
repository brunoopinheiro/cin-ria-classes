class Tire:

    @property
    def width(self) -> float:
        return self.__width

    @property
    def radius(self) -> float:
        return self.__radius

    @property
    def rotations(self) -> int:
        return self.__rotations

    @rotations.setter
    def rotations(self, _rotations) -> None:
        self.__rotations = _rotations

    @property
    def size(self) -> float:
        return round((self.width * self.radius / 10))

    def __init__(
        self,
        width: float,
        radius: float,
    ) -> None:
        self.__width = width
        self.__radius = radius
