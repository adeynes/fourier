from typing import *
import abc

from FourierSeries import FourierSeries


class OutputController(abc.ABC):
    @abc.abstractmethod
    def output(self, fourier_series: FourierSeries) -> None:
        pass
