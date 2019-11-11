from typing import *

import numpy as np
import cv2

import math

from InputController import InputController


class DrawingInputController(InputController):
    def bounds(self) -> Tuple[float, float]:
        return 0, 1

    _WINDOW_NAME: str = "USER INPUT"
    _init: bool = False  # True when there is an input in memory (can be False even with an input, as long as it is
                         # flagged for deletion)
    _pixels: List[complex] = []  # The drawn pixels as x + yj, in chronological order
    _image: np.ndarray = np.zeros((512, 1024, 3), np.uint8)  # For rendering with cv2

    def input(self, t: float) -> complex:
        self.input_ask()
        return self._pixels[math.floor(t * len(self._pixels))]

    # Ask the user for their drawing
    def input_ask(self):
        if not self._init:
            self.reset()
            self._init = True

            cv2.namedWindow(self._WINDOW_NAME)
            cv2.setMouseCallback(self._WINDOW_NAME, self.drawing_event)

            while True:
                cv2.imshow(self._WINDOW_NAME, self._image)
                key: int = cv2.waitKey(1) & 0xFF
                if key == 13:  # ENTER -> finish drawing
                    cv2.destroyAllWindows()
                    break
                if key == 27:  # ESC -> restart drawing
                    self._init = False
                    self.input_ask()
                    break

    _is_drawing: bool = False

    def drawing_event(self, event: int, x: int, y: int, flags: int, param) -> None:
        if event == cv2.EVENT_LBUTTONDOWN:
            self._is_drawing = True
            self._pixels.append(complex(x, y))
            cv2.circle(self._image, (x, y), 1, (255, 255, 255))

        if event == cv2.EVENT_MOUSEMOVE and self._is_drawing:
            self._pixels.append(complex(x, y))
            cv2.circle(self._image, (x, y), 1, (255, 255, 255))

        if event == cv2.EVENT_LBUTTONUP:
            self._is_drawing = False

    def reset(self) -> None:
        cv2.destroyAllWindows()
        self._is_drawing = False
        self._pixels = []
        self._image = np.zeros((512, 1024, 3), np.uint8)
        self._init = False

