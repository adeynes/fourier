from typing import *
from abc import ABC, abstractmethod


class InputController(ABC):
    @abstractmethod
    def bounds(self) -> Tuple[float, float]:
        pass

    @abstractmethod
    def input(self, t: float) -> complex:
        pass
