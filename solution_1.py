# solution cell
from math import pi


class VolumeCalculator:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def volume(self) -> float | None:
        if self.radius is None or self.radius <= 0:
            return None

        return (4 / 3) * pi * (self.radius ** 3)
