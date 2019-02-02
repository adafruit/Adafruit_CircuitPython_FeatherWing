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
`adafruit_featherwing.dotstar_featherwing`
====================================================

Helper for using the `Dotstar FeatherWing <https://www.adafruit.com/product/3449>`_.

* Author(s): Melissa LeBlanc-Williams
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_FeatherWing.git"

import board
import adafruit_dotstar as dotstar

class DotStarFeatherWing:
    """Class representing a `DotStar FeatherWing
       <https://www.adafruit.com/product/3449>`_.

       The feather uses pins D13 and D11"""
    def __init__(self, clock=board.D13, data=board.D11, brightness=0.2):
        """
            :param pin clock: The clock pin for the featherwing
            :param pin data: The data pin for the featherwing
            :param float brightness: Optional brightness (0.0-1.0) that defaults to 1.0
        """
        self.rows = 6
        self.columns = 12
        self._brightness = brightness
        self._dotstar = dotstar.DotStar(clock, data, self.rows * self.columns,
                                        brightness=self._brightness)

    def __setitem__(self, indices, value):
        x, y = indices
        self._dotstar[y * self.columns + x] = value

    def __getitem__(self, indices):
        x, y = indices
        return self._dotstar[y * self.columns + x]

    def fill(self, color):
        """Fills the wing with a color.
           Does NOT update the LEDs.

           :param (int, int, int) color: the color to fill with
        """
        self._dotstar.fill(color)
