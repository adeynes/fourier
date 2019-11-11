from typing import *

import cmath


class FourierSeries:
    # (frequency, coefficient)
    # Length is guaranteed to be odd: 0, 1, -1, 2, -2, ..., n, -n
    coefficients: Dict[int, complex] = {}

    def __init__(self, coefficients: Dict[int, complex]):
        self.coefficients = coefficients

    # Yields the "partial sum" of vectors at each step (converges to the actual point at that step):
    # +->+
    # |  +--->+
    # |       |
    # |      <+
    # |
    # |
    # +
    # -> [3+7j, 8+6j, 6+3j]
    def partial_sums(self, num_steps: int = 1000) -> Generator[List[complex], None, None]:
        for t in range(num_steps):
            counter: int = 0
            psums: List[complex] = []

            # n_ will be (frequency, coefficient) -> we sort by frequency: constant, 1Hz, -1Hz, 2Hz, etc
            for n, coefficient in sorted(self.coefficients.items(), key=lambda n_: abs(n_[0])):
                previous_psum: complex = psums[counter-1] if counter > 0 else 0
                psum: complex = previous_psum + (coefficient * cmath.exp(n * 2 * cmath.pi * 1j * t / num_steps))
                psums.append(psum)
                counter += 1

            yield psums
