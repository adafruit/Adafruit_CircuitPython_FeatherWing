# SPDX-FileCopyrightText: 2020 Foamyguy for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_featherwing.keyboard_featherwing`
====================================================

Helper for using the `Keyboard Featherwing`
<https://www.tindie.com/products/arturo182/keyboard-featherwing-qwerty-keyboard-26-lcd/>`_.

* Author(s): Foamyguy

Requires:
* adafruit_ili9341
* adafruit_stmpe610
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_FeatherWing.git"

import board
import adafruit_ili9341
from bbq10keyboard import BBQ10Keyboard
import neopixel


# pylint: disable-msg=too-few-public-methods
# pylint: disable-msg=too-many-arguments
from adafruit_featherwing.tft_featherwing import TFTFeatherWing


class KeyboardFeatherwing(TFTFeatherWing):
    """Class representing a `Keyboard Featherwing`
    <https://www.tindie.com/products/arturo182/keyboard-featherwing-qwerty-keyboard-26-lcd/>`_.

    """

    def __init__(
        self,
        spi=None,
        cs=None,
        dc=None,
        i2c=None,
        ts_cs=None,
        sd_cs=None,
        neopixel_pin=None,
    ):
        super().__init__(spi, cs, dc, ts_cs, sd_cs)

        if i2c is None:
            i2c = board.I2C()
        if neopixel_pin is None:
            neopixel_pin = board.D11

        self.display = adafruit_ili9341.ILI9341(
            self._display_bus, width=320, height=240
        )
        self.neopixel = neopixel.NeoPixel(neopixel_pin, 1)
        self.keyboard = BBQ10Keyboard(i2c)
