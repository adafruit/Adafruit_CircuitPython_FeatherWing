# SPDX-FileCopyrightText: 2019 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_featherwing.matrix_featherwing`
====================================================

Helper for using the `Adafruit 8x16 LED Matrix FeatherWing
<https://www.adafruit.com/product/3155>`_.

* Author(s): Melissa LeBlanc-Williams
"""

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_FeatherWing.git"

import board
from adafruit_ht16k33 import matrix

from adafruit_featherwing.auto_writeable import AutoWriteable

try:
    from typing import Optional, Tuple, Union
    from busio import I2C
except ImportError:
    pass


class MatrixFeatherWing(AutoWriteable):
    """Class representing an `Adafruit 8x16 LED Matrix FeatherWing
    <https://www.adafruit.com/product/3155>`_.

    Automatically uses the feather's I2C bus."""

    def __init__(self, address: int = 0x70, i2c: Optional[I2C] = None):

        if i2c is None:
            i2c = board.I2C()
        self._matrix = matrix.Matrix16x8(i2c, address)
        self._matrix.auto_write = False
        self.columns = 16
        self.rows = 8
        super().__init__()

    def __getitem__(self, key: Tuple[int, int]) -> bool:
        """
        Get the current value of a pixel
        """
        x, y = key
        return self.pixel(x, y)

    def __setitem__(self, key: Tuple[int, int], value: Union[int, bool]):
        """
        Turn a pixel off or on
        """
        x, y = key
        self.pixel(x, y, value)
        self._update()

    def _update(self):
        """
        Update the Display automatically if auto_write is set to True
        """
        if self._auto_write:
            self._matrix.show()

    def pixel(self, x: int, y: int, color: Optional[bool] = None) -> Optional[bool]:
        """
        Turn a pixel on or off or retrieve a pixel value

        :param int x: The pixel row
        :param int y: The pixel column
        :param color: Whether to turn the pixel on or off
        :type color: int or bool
        """
        value = self._matrix.pixel(x, y, color)
        self._update()
        return value

    def show(self):
        """
        Update the Pixels. This is only needed if auto_write is set to False
        This can be very useful for more advanced graphics effects.
        """
        self._matrix.show()

    def fill(self, fill: bool):
        """
        Turn all pixels on or off

        :param bool fill: True turns all pixels on, False turns all pixels off

        """
        if isinstance(fill, bool):
            self._matrix.fill(1 if fill else 0)
            self._update()
        else:
            raise ValueError("Must set to either True or False.")

    def shift_right(self, rotate: bool = False):
        """
        Shift all pixels right

        :param rotate: (Optional) Rotate the shifted pixels to the left side (default=False)
        """
        self._matrix.shift_right(rotate)
        self._update()

    def shift_left(self, rotate: bool = False):
        """
        Shift all pixels left

        :param rotate: (Optional) Rotate the shifted pixels to the right side (default=False)
        """
        self._matrix.shift_left(rotate)
        self._update()

    def shift_up(self, rotate: bool = False):
        """
        Shift all pixels up

        :param rotate: (Optional) Rotate the shifted pixels to bottom (default=False)
        """
        self._matrix.shift_up(rotate)
        self._update()

    def shift_down(self, rotate: bool = False):
        """
        Shift all pixels down

        :param rotate: (Optional) Rotate the shifted pixels to top (default=False)
        """
        self._matrix.shift_down(rotate)
        self._update()

    @property
    def blink_rate(self):
        """
        Blink Rate returns the current rate that the pixels blink.
        0 = Not Blinking
        1-3 = Successively slower blink rates
        """
        return self._matrix.blink_rate

    @blink_rate.setter
    def blink_rate(self, rate: int):
        self._matrix.blink_rate = rate

    @property
    def brightness(self):
        """
        Brightness returns the current display brightness.
        0-15 = Dimmest to Brightest Setting
        """
        return round(self._matrix.brightness * 15)

    @brightness.setter
    def brightness(self, brightness: int):
        if not 0 <= brightness <= 15:
            raise ValueError("Brightness must be a value between 0 and 15")
        self._matrix.brightness = brightness / 15
