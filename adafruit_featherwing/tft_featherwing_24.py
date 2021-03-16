# SPDX-FileCopyrightText: 2020 Melissa LeBlanc-Williams for Adafruit Industries
# SPDX-FileCopyrightText: 2020 Foamyguy for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_featherwing.tft_featherwing_24`
====================================================

Helper for using the `TFT FeatherWing 2.4"`
<https://www.adafruit.com/product/3315>`_.

* Author(s): Melissa LeBlanc-Williams, Foamyguy

Requires:
* adafruit_ili9341
* adafruit_stmpe610
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_FeatherWing.git"


import adafruit_ili9341

# pylint: disable-msg=too-few-public-methods
from adafruit_featherwing.tft_featherwing import TFTFeatherWing


class TFTFeatherWing24(TFTFeatherWing):
    """Class representing an `TFT FeatherWing 2.4
    <https://www.adafruit.com/product/3315>`_.

    """

    def __init__(self, spi=None, cs=None, dc=None):
        super().__init__(spi, cs, dc)
        self.display = adafruit_ili9341.ILI9341(
            self._display_bus, width=320, height=240
        )
