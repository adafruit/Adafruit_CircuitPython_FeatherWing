# SPDX-FileCopyrightText: 2019 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_featherwing.sevensegment_featherwing`
====================================================

Helper for using the `7-Segment LED HT16K33 FeatherWing <https://www.adafruit.com/product/3140>`_.

* Author(s): Melissa LeBlanc-Williams
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_FeatherWing.git"

import board
from adafruit_ht16k33 import segments
from adafruit_featherwing.led_segments import Segments

try:
    from typing import Optional
    from busio import I2C
except ImportError:
    pass


class SevenSegmentFeatherWing(Segments):
    """Class representing an `Adafruit 7-Segment LED HT16K33 FeatherWing
    <https://www.adafruit.com/product/3140>`_.

    Automatically uses the feather's I2C bus."""

    def __init__(self, address: int = 0x70, i2c: Optional[I2C] = None):
        super().__init__()
        if i2c is None:
            i2c = board.I2C()
        self._segments = segments.Seg7x4(i2c, address)
        self._segments.auto_write = False
