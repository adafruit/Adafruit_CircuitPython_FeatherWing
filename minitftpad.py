# The MIT License (MIT)
#
# Copyright (c) 2019 for Adafruit Industries LLC
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

# We have a lot of attributes for this complex library.
# pylint: disable=too-many-instance-attributes

"""
Adafruit Mini Color TFT with Joystick FeatherWing
`adafruit_featherwing.minitftpad`
====================================================

CircuitPython driver for `Mini Color TFT with Joystick FeatherWing
<https://www.adafruit.com/product/3321>`_.

* Author(s): Kattni Rembor, Scott Shawcroft, Radomir Dopieralski, Michael McWethy, Jonah Yolles-Murphy, Melissa LeBlanc-Williams
"""

from adafruit_seesaw import digitalio as dio
from adafruit_seesaw import seesaw as ss
from adafruit_seesaw import pwmout as pwm
import displayio
from micropython import const
import board
import sys
# pylint: disable=wrong-import-position
try:
    lib_index = sys.path.index("/lib")        # pylint: disable=invalid-name
    if lib_index < sys.path.index(".frozen"):
        # Prefer frozen modules over those in /lib.
        sys.path.insert(lib_index, ".frozen")
except ValueError:
    # Don't change sys.path if it doesn't contain "lib" or ".frozen".
    pass

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_FeatherWing.git"

_INIT_SEQUENCE = bytearray(
    b"\x01\x80\x96"  # SWRESET and Delay 150ms
    b"\x11\x80\xff"  # SLPOUT and Delay
    b"\xb1\x03\x01\x2C\x2D"  # _FRMCTR1
    b"\xb2\x03\x01\x2C\x2D"  # _FRMCTR2
    b"\xb3\x06\x01\x2C\x2D\x01\x2C\x2D"  # _FRMCTR3
    b"\xb4\x01\x07"  # _INVCTR line inversion
    b"\xc0\x03\xa2\x02\x84"  # _PWCTR1 GVDD = 4.7V, 1.0uA
    b"\xc1\x01\xc5"  # _PWCTR2 VGH=14.7V, VGL=-7.35V
    b"\xc2\x02\x0a\x00"  # _PWCTR3 Opamp current small, Boost frequency
    b"\xc3\x02\x8a\x2a"
    b"\xc4\x02\x8a\xee"
    b"\xc5\x01\x0e"  # _VMCTR1 VCOMH = 4V, VOML = -1.1V
    b"\x20\x00"  # _INVOFF
    b"\x36\x01\x18"  # _MADCTL bottom to top refresh
    # 1 clk cycle nonoverlap, 2 cycle gate rise, 3 sycle osc equalie,
    # fix on VTL
    b"\x3a\x01\x05"  # COLMOD - 16bit color
    b"\xe0\x10\x02\x1c\x07\x12\x37\x32\x29\x2d\x29\x25\x2B\x39\x00\x01\x03\x10"  # _GMCTRP1 Gamma
    b"\xe1\x10\x03\x1d\x07\x06\x2E\x2C\x29\x2D\x2E\x2E\x37\x3F\x00\x00\x02\x10"  # _GMCTRN1
    b"\x13\x80\x0a"  # _NORON
    b"\x29\x80\x64"  # _DISPON
    b"\x36\x01\xC0"  # _MADCTL Default rotation plus BGR encoding
)


class Minitftpad:     # pylint: disable=too-many-public-methods
    """Represents a single mini tft featherwing. Do not use more than one at
       a time."""
    def __init__(self, _disp_spi=board.SPI(), _disp_i2c=board.I2C(), _disp_cs=board.D5, _disp_dc=board.D6, adress=0x5E):

        # SPI
        self._disp_spi = _disp_spi
        # DS and CS pins
        self._disp_cs = _disp_cs
        self._disp_dc = _disp_dc

        # I2C
        self._i2c = _disp_i2c
        self._seesaw = ss.Seesaw(self._i2c, adress)
        self._backlight_pin = pwm.PWMOut(self._seesaw, 5)

        # initilise stuff
        self._disp_rst_pin = dio.DigitalIO(self._seesaw, 8)
        self._disp_rst = (self._disp_rst_pin)

        # start backlight in on position
        self._backlite = (self._backlight_pin)
        self._backlite.duty_cycle = 0

        # setup the display
        displayio.release_displays()
        self._display_bus = displayio.FourWire(self._disp_spi, command=self._disp_dc, chip_select=self._disp_cs, reset=self._disp_rst.value)
        self.display = displayio.Display(self._display_bus, _INIT_SEQUENCE, width=160, height=80, colstart=24, rotation=270)


        # pylint: disable=bad-whitespace
        self._BUTTON_RIGHT = const(7)
        self._BUTTON_DOWN = const(4)
        self._BUTTON_UP = const(2)
        self._BUTTON_LEFT = const(3)
        self._BUTTON_B = const(9)
        self._BUTTON_A = const(10)
        self._BUTTON_SEL = const(11)
        # pylint: enable=bad-whitespace
        self._button_mask = const((1 << self._BUTTON_RIGHT) |
                            (1 << self._BUTTON_DOWN) |
                            (1 << self._BUTTON_UP) |
                            (1 << self._BUTTON_LEFT) |
                            (1 << self._BUTTON_B) |
                            (1 << self._BUTTON_A) |
                            (1 << self._BUTTON_SEL))
        self._seesaw.pin_mode_bulk(self._button_mask, self._seesaw.INPUT_PULLUP)

        # initilise stuff
    @property
    def backlight(self):
        return self._backlite.duty_cycle

    @backlight.setter
    def backlight(self, value):
        self._backlite.duty_cycle = int(255 * max(0, min(1, (1-value))))

    @property
    def button_up(self):
        buttons = self._seesaw.digital_read_bulk(self._button_mask)
        if not buttons & (1 << self._BUTTON_UP):
            return True
        else:
            return False

    @property
    def button_down(self):
        buttons = self._seesaw.digital_read_bulk(self._button_mask)
        if not buttons & (1 << self._BUTTON_DOWN):
            return True
        else:
            return False

    @property
    def button_right(self):
        buttons = self._seesaw.digital_read_bulk(self._button_mask)
        if not buttons & (1 << self._BUTTON_RIGHT):
            return True
        else:
            return False

    @property
    def button_left(self):
        buttons = self._seesaw.digital_read_bulk(self._button_mask)
        if not buttons & (1 << self._BUTTON_LEFT):
            return True
        else:
            return False

    @property
    def button_a(self):
        buttons = self._seesaw.digital_read_bulk(self._button_mask)
        if not buttons & (1 << self._BUTTON_A):
            return True
        else:
            return False

    @property
    def button_b(self):
        buttons = self._seesaw.digital_read_bulk(self._button_mask)
        if not buttons & (1 << self._BUTTON_B):
            return True
        else:
            return False

    @property
    def button_sel(self):
        buttons = self._seesaw.digital_read_bulk(self._button_mask)
        if not buttons & (1 << self._BUTTON_SEL):
            return True
        else:
            return False

wing = Minitftpad() # pylint: disable=invalid-name
"""Object that is automatically created on import.

   To use, simply import it from the module:

   .. code-block:: python

     from adafruit_featherwing.minitftpad import wing, displayio
"""
