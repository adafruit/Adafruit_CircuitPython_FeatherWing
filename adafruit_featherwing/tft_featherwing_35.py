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

from adafruit_hx8357 import HX8357

# pylint: disable-msg=too-few-public-methods
from adafruit_featherwing.tft_featherwing import TFTFeatherWing


class TFTFeatherWing35(TFTFeatherWing):
    """Class representing an `TFT FeatherWing 3.5
    <https://www.adafruit.com/product/3651>`_.

    """

    def __init__(self, spi=None, cs=None, dc=None):
        super().__init__(spi, cs, dc)
        self.display = HX8357(self._display_bus, width=480, height=320)
