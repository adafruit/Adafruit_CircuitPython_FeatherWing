# SPDX-FileCopyrightText: 2020 Melissa LeBlanc-Williams for Adafruit Industries
# SPDX-FileCopyrightText: 2020 Foamyguy for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_featherwing.tft_featherwing_35`
====================================================

Helper for using the `TFT FeatherWing 3.5"`
<https://www.adafruit.com/product/3651>`_.

* Author(s): Melissa LeBlanc-Williams, Foamyguy

Requires:
* adafruit_hx8357
* adafruit_stmpe610
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_FeatherWing.git"

import board
import digitalio
import displayio
from adafruit_hx8357 import HX8357
from adafruit_stmpe610 import Adafruit_STMPE610_SPI
import sdcardio
import storage

# pylint: disable-msg=too-few-public-methods
class TFTFeatherWing35:
    """Class representing an `TFT FeatherWing 3.5
    <https://www.adafruit.com/product/3651>`_.

    """

    def __init__(self, spi=None, cs=None, dc=None):
        displayio.release_displays()
        if spi is None:
            spi = board.SPI()
        if cs is None:
            cs = board.D9
        if dc is None:
            dc = board.D10

        ts_cs = digitalio.DigitalInOut(board.D6)
        self.touchscreen = Adafruit_STMPE610_SPI(spi, ts_cs)

        display_bus = displayio.FourWire(spi, command=dc, chip_select=cs)
        self.display = HX8357(display_bus, width=480, height=320)

        sd_cs = board.D5
        self._sdcard = None
        try:
            self._sdcard = sdcardio.SDCard(spi, sd_cs)
            vfs = storage.VfsFat(self._sdcard)
            storage.mount(vfs, "/sd")
        except OSError as error:
            print("No SD card found:", error)
