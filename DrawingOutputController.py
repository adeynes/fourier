from typing import *

import cv2
from _math_utils import *

from FourierSeries import FourierSeries
from OutputController import OutputController


class DrawingOutputController(OutputController):
    _WINDOW_NAME = "FOURIER SERIES PLOT"

    def output(self, fourier_series: FourierSeries, num_steps: int = 1000) -> None:
        cv2.namedWindow(self._WINDOW_NAME)

        terminal_points: List[complex] = []  # the points to which the psums converge, i.e. the last psums for each t

        t: int = 0
        for partial_sums in fourier_series.partial_sums(num_steps):
            plot: np.ndarray = np.zeros((512, 1024, 3), np.uint8)
            c2t: Callable[[complex], int] = complex_to_rounded_tuple
            last_point = point = 0 + 0j

            for tpoint in terminal_points:
                cv2.circle(plot, c2t(tpoint), 1, (255, 255, 255))

            for i, point in enumerate(partial_sums):
                cv2.arrowedLine(plot, c2t(last_point), c2t(point), (0, 0, 255), 1)
                last_point = point

            terminal_points.append(point)

            t += 1

            cv2.imshow(self._WINDOW_NAME, plot)
            cv2.waitKey(2)
            if t == num_steps:
                cv2.waitKey(0)

        cv2.destroyAllWindows()

