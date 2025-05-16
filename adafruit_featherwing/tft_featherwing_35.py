# SPDX-FileCopyrightText: 2020 Melissa LeBlanc-Williams for Adafruit Industries
# SPDX-FileCopyrightText: 2020 Foamyguy for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_featherwing.tft_featherwing_35`
====================================================

Helper for using the `TFT FeatherWing 3.5"
<https://www.adafruit.com/product/3651>`_.

* Author(s): Melissa LeBlanc-Williams, Foamyguy

Requires:
* adafruit_hx8357
* adafruit_stmpe610
"""

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_FeatherWing.git"

import board
from adafruit_hx8357 import HX8357

from adafruit_featherwing.tft_featherwing import TFTFeatherWing

try:
    from typing import Optional

    from busio import I2C, SPI
    from microcontroller import Pin
except ImportError:
    pass


class TFTFeatherWing35(TFTFeatherWing):
    """Class representing a TFT FeatherWing 3.5 V1
    Attempts to mount the SD card to /sd.
    """

    def __init__(
        self,
        spi: Optional[SPI] = None,
        cs: Optional[Pin] = None,
        dc: Optional[Pin] = None,
        ts_cs: Optional[Pin] = None,
        sd_cs: Optional[Pin] = None,
    ):
        super().__init__(
            spi, cs_pin=cs, dc_pin=dc, ts_cs_pin=ts_cs, sd_cs_pin=sd_cs, resistive=True
        )
        self.display = HX8357(self._display_bus, width=480, height=320)
        """Display object for the FeatherWing's screen."""


class TFTFeatherWing35V2(TFTFeatherWing):
    """Class representing a `TFT FeatherWing 3.5 V2
    <https://www.adafruit.com/product/3651>`_.
    Attempts to mount the SD card to /sd.
    """

    def __init__(
        self,
        spi: Optional[SPI] = None,
        cs_pin: Optional[Pin] = None,
        dc_pin: Optional[Pin] = None,
        sd_cs_pin: Optional[Pin] = None,
        i2c: Optional[I2C] = None,
    ):
        if i2c is None:
            i2c = board.I2C()
        super().__init__(
            spi,
            cs_pin=cs_pin,
            dc_pin=dc_pin,
            sd_cs_pin=sd_cs_pin,
            i2c=i2c,
            resistive=True,
        )
        self.display = HX8357(self._display_bus, width=480, height=320)
        """Display object for the FeatherWing's screen."""
