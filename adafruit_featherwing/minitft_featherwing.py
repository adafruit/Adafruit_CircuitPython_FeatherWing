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
`adafruit_featherwing.minitft_featherwing`
====================================================

Helper for using the `Mini Color TFT with Joystick FeatherWing
<https://www.adafruit.com/product/3321>`_.

* Author(s): Melissa LeBlanc-Williams
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_FeatherWing.git"

from collections import namedtuple
import board
from micropython import const
from adafruit_seesaw.seesaw import Seesaw
from adafruit_seesaw.pwmout import PWMOut
import displayio
from adafruit_st7735r import ST7735R

BUTTON_RIGHT = const(7)
BUTTON_DOWN = const(4)
BUTTON_LEFT = const(3)
BUTTON_UP = const(2)
BUTTON_SEL = const(11)
BUTTON_A = const(10)
BUTTON_B = const(9)

Buttons = namedtuple("Buttons", "up down left right a b select")


class MiniTFTFeatherWing:
    """Class representing an `Mini Color TFT with Joystick FeatherWing
       <https://www.adafruit.com/product/3321>`_.

       Automatically uses the feather's I2C bus."""

    _button_mask = (
        (1 << BUTTON_RIGHT)
        | (1 << BUTTON_DOWN)
        | (1 << BUTTON_LEFT)
        | (1 << BUTTON_UP)
        | (1 << BUTTON_SEL)
        | (1 << BUTTON_A)
        | (1 << BUTTON_B)
    )
    # pylint: disable-msg=too-many-arguments
    def __init__(self, address=0x5E, i2c=None, spi=None, cs=None, dc=None):
        displayio.release_displays()
        if i2c is None:
            i2c = board.I2C()
        if spi is None:
            spi = board.SPI()
        if cs is None:
            cs = board.D5
        if dc is None:
            dc = board.D6
        self._ss = Seesaw(i2c, address)
        self._ss.pin_mode_bulk(self._button_mask, self._ss.INPUT_PULLUP)
        self._ss.pin_mode(8, self._ss.OUTPUT)
        self._ss.digital_write(8, True)  # Reset the Display via Seesaw
        self._backlight = PWMOut(self._ss, 5)
        self._backlight.duty_cycle = 0
        display_bus = displayio.FourWire(spi, command=dc, chip_select=cs)
        self.display = ST7735R(
            display_bus, width=160, height=80, colstart=24, rotation=270, bgr=True
        )

    # pylint: enable-msg=too-many-arguments

    @property
    def backlight(self):
        """
        Return the current backlight duty cycle value
        """
        return self._backlight.duty_cycle / 255

    @backlight.setter
    def backlight(self, brightness):
        """
        Set the backlight duty cycle
        """
        self._backlight.duty_cycle = int(255 * min(max(brightness, 0.0), 1.0))

    @property
    def buttons(self):
        """
        Return a set of buttons with current push values
        """
        try:
            button_values = self._ss.digital_read_bulk(self._button_mask)
        except OSError:
            return Buttons(
                *[
                    False
                    for button in (
                        BUTTON_UP,
                        BUTTON_DOWN,
                        BUTTON_LEFT,
                        BUTTON_RIGHT,
                        BUTTON_A,
                        BUTTON_B,
                        BUTTON_SEL,
                    )
                ]
            )
        return Buttons(
            *[
                not button_values & (1 << button)
                for button in (
                    BUTTON_UP,
                    BUTTON_DOWN,
                    BUTTON_LEFT,
                    BUTTON_RIGHT,
                    BUTTON_A,
                    BUTTON_B,
                    BUTTON_SEL,
                )
            ]
        )
