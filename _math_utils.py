from typing import *

import numpy as np


def integral(func: Callable[[float], complex], bounds: Tuple[float, float] = (0, 1), delta: float = 0.001) -> complex:
    return sum([func(bounds[0] + delta * i) for i in range(int((bounds[1] - bounds[0]) / delta))]) * delta


def complex_to_rounded_tuple(z: complex) -> Tuple[int, int]:
    return round(z.real), round(z.imag)


# [3+1j, -4j, 2+1.5j, -6+1j] -> ([3., 0., 2., -6.], [1., -4., 1.5, 1.])
def complex_list_to_coordinate_lists(complex_list: List[complex]) -> Tuple[List[float], List[float]]:
    # real_parts: List[float] = []
    # imag_parts: List[float] = []
    # for num in complex_list:
    #     real_parts.append(num.real)
    #     imag_parts.append(num.imag)
    # return (real_parts, imag_parts)

    complex_as_list: List[List[float]] = np.array([[complex_.real, complex_.imag] for complex_ in complex_list])
    coord_lists: Tuple[List[float], List[float]] = (complex_as_list[:,0], complex_as_list[:,1])
    return coord_lists
