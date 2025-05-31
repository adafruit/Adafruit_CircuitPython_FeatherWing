# SPDX-FileCopyrightText: 2020 Melissa LeBlanc-Williams for Adafruit Industries
# SPDX-FileCopyrightText: 2020 Foamyguy for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_featherwing.tft_featherwing`
====================================================

Super class for helpers for using the TFT FeatherWing devices
see tft_featherwng_24 and tft_featherwing_35

* Author(s): Melissa LeBlanc-Williams, Foamyguy

Requires:
* adafruit_stmpe610
"""

import time

import board
import digitalio
import displayio
import fourwire

try:
    from adafruit_stmpe610 import Adafruit_STMPE610_SPI
except ImportError:
    pass
try:
    from adafruit_tsc2007 import TSC2007
except ImportError:
    pass
try:
    from adafruit_focaltouch import Adafruit_FocalTouch
except ImportError:
    pass

import sdcardio
import storage

try:
    from typing import Optional

    from busio import I2C, SPI
    from microcontroller import Pin
except ImportError:
    pass


class TFTFeatherWing:
    """Base class for TFT FeatherWings."""

    def __init__(
        self,
        spi: Optional[SPI] = None,
        i2c: Optional[I2C] = None,
        cs_pin: Optional[Pin] = None,
        dc_pin: Optional[Pin] = None,
        ts_cs_pin: Optional[Pin] = None,
        sd_cs_pin: Optional[Pin] = None,
        irq_pin: Optional[Pin] = None,
        resistive: Optional[bool] = True,
    ):
        # Initialize Display Bus
        displayio.release_displays()
        if spi is None:
            spi = board.SPI()
        if cs_pin is None:
            cs_pin = board.D9
        if dc_pin is None:
            dc_pin = board.D10

        self._display_bus = fourwire.FourWire(spi, command=dc_pin, chip_select=cs_pin)

        # Initialize SD Card
        if sd_cs_pin is None:
            sd_cs_pin = board.D5

        self._sdcard = None
        try:
            self._sdcard = sdcardio.SDCard(spi, sd_cs_pin)
            vfs = storage.VfsFat(self._sdcard)
            storage.mount(vfs, "/sd")
        except OSError as error:
            print("No SD card found:", error)

        # Initialize Touchscreen
        self.touchscreen = None
        if resistive:
            if i2c is None:  # STMPE610
                if ts_cs_pin is None:
                    ts_cs_pin = board.D6
                ts_cs = digitalio.DigitalInOut(ts_cs_pin)
                try:
                    # the screen might not be ready from cold boot
                    time.sleep(0.8)
                    self.touchscreen = Adafruit_STMPE610_SPI(spi, ts_cs)
                except RuntimeError:
                    # wait and try once more
                    time.sleep(1.0)
                    self.touchscreen = Adafruit_STMPE610_SPI(spi, ts_cs)
            else:  # TSC2007
                if irq_pin is None:
                    irq_pin = board.D6
                irq = digitalio.DigitalInOut(irq_pin)
                self.touchscreen = TSC2007(i2c, irq=irq)
        else:  # FocalTouch
            if irq_pin is None:
                irq_pin = board.D6
            self.touchscreen = Adafruit_FocalTouch(i2c, irq_pin=irq_pin)
