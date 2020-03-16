# The MIT License (MIT)
#
# Copyright (c) 2019 Melissa LeBlanc-Williams for Adafruit Industries LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_featherwing.neopixel_featherwing`
====================================================

Helper for using the `NeoPixel FeatherWing <https://www.adafruit.com/product/2945>`_.

* Author(s): Melissa LeBlanc-Williams
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_FeatherWing.git"

import board
import neopixel
from adafruit_featherwing.pixelmatrix import PixelMatrix


class NeoPixelFeatherWing(PixelMatrix):
    """Class representing a `NeoPixel FeatherWing
       <https://www.adafruit.com/product/2945>`_.

       The feather uses pins D6 by default"""

    def __init__(self, pixel_pin=board.D6, brightness=0.1):
        """
            :param pin pixel_pin: The pin for the featherwing
            :param float brightness: Optional brightness (0.0-1.0) that defaults to 1.0
        """
        super().__init__()
        self.rows = 4
        self.columns = 8
        self._matrix = neopixel.NeoPixel(
            pixel_pin,
            self.rows * self.columns,
            brightness=brightness,
            auto_write=False,
            pixel_order=neopixel.GRB,
        )

    def shift_up(self, rotate=False):
        """
        Shift all pixels up

        :param rotate: (Optional) Rotate the shifted pixels to bottom (default=False)

        This example shifts 2 pixels up

        .. code-block:: python

            import time
            from adafruit_featherwing import neopixel_featherwing

            neopixel = neopixel_featherwing.NeoPixelFeatherWing()

            # Draw Red and Green Pixels
            neopixel[4, 1] = (255, 0, 0)
            neopixel[5, 1] = (0, 255, 0)

            # Rotate it off the screen
            for i in range(0, neopixel.rows - 1):
                neopixel.shift_up(True)
                time.sleep(.1)

            time.sleep(1)
            # Shift it off the screen
            for i in range(0, neopixel.rows - 1):
                neopixel.shift_up()
                time.sleep(.1)

        """
        super().shift_down(rotate)  # Up and down are reversed

    def shift_down(self, rotate=False):
        """
        Shift all pixels down.

        :param rotate: (Optional) Rotate the shifted pixels to top (default=False)

        This example shifts 2 pixels down

        .. code-block:: python

            import time
            from adafruit_featherwing import neopixel_featherwing

            neopixel = neopixel_featherwing.NeoPixelFeatherWing()

            # Draw Red and Green Pixels
            neopixel[4, 1] = (255, 0, 0)
            neopixel[5, 1] = (0, 255, 0)

            # Rotate it off the screen
            for i in range(0, neopixel.rows - 1):
                neopixel.shift_down(True)
                time.sleep(.1)

            time.sleep(1)
            # Shift it off the screen
            for i in range(0, neopixel.rows - 1):
                neopixel.shift_down()
                time.sleep(.1)

        """
        super().shift_up(rotate)  # Up and down are reversed
