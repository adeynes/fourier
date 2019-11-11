from typing import *

import cmath
from _math_utils import *

from FourierSeries import FourierSeries
from InputController import InputController


# Vectors run from -num_vectors to num_vectors -> there are actually 2*num_vectors + 1 vectors
def fourier_series(input_: InputController, num_vectors: int = 500) -> FourierSeries:
    vectors: Dict[int, complex] = {}
    for n in range(-num_vectors, num_vectors + 1):
        vectors[n] = integral(lambda t: input_.input(t) * cmath.exp(-n * 2 * cmath.pi * 1j * t), input_.bounds(), 0.001)
    return FourierSeries(vectors)
