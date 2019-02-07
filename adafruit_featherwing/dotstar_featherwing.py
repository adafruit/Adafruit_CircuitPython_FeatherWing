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
#pylint: disable-msg=unsubscriptable-object, unsupported-assignment-operation

class PixelMatrixFeatherWing:
    """Base Class for DotStar and NeoPixel FeatherWings

       The feather uses pins D13 and D11"""
    def __init__(self):
        self.rows = 0
        self.columns = 0
        self._matrix = None
        self._auto_write = True

    def __setitem__(self, indices, value):
        """
        indices can be one of three things:
            x and y ints that are calculated to the DotStar index
            a slice of DotStar indexes with a set of values that match the slice
            a single int that specifies the DotStar index
        value can be one of three things:
                a (r,g,b) list/tuple
                a (r,g,b, brightness) list/tuple
                a single, longer int that contains RGB values, like 0xFFFFFF
            brightness, if specified should be a float 0-1
        """
        self._matrix[self._get_index(indices)] = value
        self._update()

    def __getitem__(self, indices):
        """
        indices can be one of three things:
            x and y ints that are calculated to the DotStar index
            a slice of DotStar indexes to retrieve
            a single int that specifies the DotStar index
        """
        return self._matrix[self._get_index(indices)]

    def _get_index(self, indices):
        """
        Figure out which DotStar to address based on what was passed in
        """
        if isinstance(indices, int):
            if not 0 <= indices < self.rows * self.columns:
                raise ValueError('The index of {} is out of range'.format(indices))
            return indices
        elif isinstance(indices, slice):
            return indices
        elif len(indices) == 2:
            x, y = indices
            if not 0 <= x < self.columns:
                raise ValueError('The X value of {} is out of range'.format(x))
            if not 0 <= y < self.rows:
                raise ValueError('The Y value of {} is out of range'.format(y))
            return y * self.columns + x
        else:
            raise ValueError('Index must be 1 or 2 number')

    def _update(self):
        """
        Update the Display automatically if auto_write is set to True
        """
        if self._auto_write:
            self._matrix.show()

    def _fill(self, color=0):
        """
        Fills all of the Pixels with a color or unlit if empty.
        """
        self._matrix.fill(color)
        self._update()

    def _show(self):
        """
        Update the Pixels. This is only needed if auto_write is set to False
        This can be very useful for more advanced graphics effects.
        """
        self._matrix.show()

    def _shift_right(self, rotate=False):
        """
        Shift all pixels right
        """
        for y in range(0, self.rows):
            last_pixel = self._matrix[(y + 1) * self.columns - 1] if rotate else 0
            for x in range(self.columns - 1, 0, -1):
                self._matrix[y * self.columns + x] = self._matrix[y * self.columns + x - 1]
            self._matrix[y * self.columns] = last_pixel
        self._update()

    def _shift_left(self, rotate=False):
        """
        Shift all pixels left
        """
        for y in range(0, self.rows):
            last_pixel = self._matrix[y * self.columns] if rotate else 0
            for x in range(0, self.columns - 1):
                self._matrix[y * self.columns + x] = self._matrix[y * self.columns + x + 1]
            self._matrix[(y + 1) * self.columns - 1] = last_pixel
        self._update()

    def _shift_up(self, rotate=False):
        """
        Shift all pixels up
        """
        for x in range(0, self.columns):
            last_pixel = self._matrix[(self.rows - 1) * self.columns + x] if rotate else 0
            for y in range(self.rows - 1, 0, -1):
                self._matrix[y * self.columns + x] = self._matrix[(y - 1) * self.columns + x]
            self._matrix[x] = last_pixel
        self._update()

    def _shift_down(self, rotate=False):
        """
        Shift all pixels down
        """
        for x in range(0, self.columns):
            last_pixel = self._matrix[x] if rotate else 0
            for y in range(0, self.rows - 1):
                self._matrix[y * self.columns + x] = self._matrix[(y + 1) * self.columns + x]
            self._matrix[(self.rows - 1) * self.columns + x] = last_pixel
        self._update()

class DotStarFeatherWing(PixelMatrixFeatherWing):
    """Class representing a `DotStar FeatherWing
       <https://www.adafruit.com/product/3449>`_.

       The feather uses pins D13 and D11"""
    def __init__(self, clock=board.D13, data=board.D11, brightness=0.2):
        """
            :param pin clock: The clock pin for the featherwing
            :param pin data: The data pin for the featherwing
            :param float brightness: Optional brightness (0.0-1.0) that defaults to 1.0
        """
        super().__init__()
        self.rows = 6
        self.columns = 12
        self._matrix = dotstar.DotStar(clock, data, self.rows * self.columns,
                                       brightness=brightness, auto_write=False)

    def fill(self, color=0):
        """
        Fills all of the DotStars with a color or unlit if empty.

        :param color: (Optional) The text or number to display (default=0)
        :type color: list/tuple or int

        This example shows various ways of using the fill() function

        .. code-block:: python

            import time
            from adafruit_featherwing import dotstar_featherwing

            dotstar = dotstar_featherwing.DotStarFeatherWing()
            dotstar.fill((255, 255, 255)) # Fill White
            time.sleep(1)
            dotstar.fill((255, 255, 255, 0.5)) # Fill White Half Brightness
            time.sleep(1)
            dotstar.fill(0xFF0000) # Fill Red
            time.sleep(1)
            dotstar.fill() # Clear all lit DotStars

        """
        super()._fill(color)

    def show(self):
        """
        Update the DotStars. This is only needed if auto_write is set to False
        This can be very useful for more advanced graphics effects.

        This example changes the blink rate and prints out the current setting

        .. code-block:: python

            import time
            from adafruit_featherwing import dotstar_featherwing

            dotstar = dotstar_featherwing.DotStarFeatherWing()
            dotstar.fill() # Clear any lit Dotstars
            dotstar.auto_write = False
            dotstar[0, 0] = (255, 255, 255) # Set White
            time.sleep(1)
            dotstar.show() # Update the DotStars

        """
        super()._show()

    def shift_right(self, rotate=False):
        """
        Shift all pixels right

        :param rotate: (Optional) Rotate the shifted pixels to the left side (default=False)

        This example shifts 2 pixels to the right

        .. code-block:: python

            import time
            from adafruit_featherwing import dotstar_featherwing

            dotstar = dotstar_featherwing.DotStarFeatherWing()

            # Draw Red and Green Pixels
            dotstar[5, 3] = (255, 0, 0)
            dotstar[6, 3] = (0, 255, 0)

            # Rotate it off the screen
            for i in range(0, dotstar.columns - 1):
                dotstar.shift_right(True)
                time.sleep(.1)

            time.sleep(1)
            # Shift it off the screen
            for i in range(0, dotstar.columns - 1):
                dotstar.shift_right()
                time.sleep(.1)

        """
        super()._shift_right(rotate)

    def shift_left(self, rotate=False):
        """
        Shift all pixels left

        :param rotate: (Optional) Rotate the shifted pixels to the right side (default=False)

        This example shifts 2 pixels to the left

        .. code-block:: python

            import time
            from adafruit_featherwing import dotstar_featherwing

            dotstar = dotstar_featherwing.DotStarFeatherWing()

            # Draw Red and Green Pixels
            dotstar[5, 3] = (255, 0, 0)
            dotstar[6, 3] = (0, 255, 0)

            # Rotate it off the screen
            for i in range(0, dotstar.columns - 1):
                dotstar.shift_left(True)
                time.sleep(.1)

            time.sleep(1)
            # Shift it off the screen
            for i in range(0, dotstar.columns - 1):
                dotstar.shift_left()
                time.sleep(.1)

        """
        super()._shift_left(rotate)

    def shift_up(self, rotate=False):
        """
        Shift all pixels up

        :param rotate: (Optional) Rotate the shifted pixels to bottom (default=False)

        This example shifts 2 pixels up

        .. code-block:: python

            import time
            from adafruit_featherwing import dotstar_featherwing

            dotstar = dotstar_featherwing.DotStarFeatherWing()

            # Draw Red and Green Pixels
            dotstar[5, 3] = (255, 0, 0)
            dotstar[6, 3] = (0, 255, 0)

            # Rotate it off the screen
            for i in range(0, dotstar.rows - 1):
                dotstar.shift_up(True)
                time.sleep(.1)

            time.sleep(1)
            # Shift it off the screen
            for i in range(0, dotstar.rows - 1):
                dotstar.shift_up()
                time.sleep(.1)

        """
        super()._shift_up(rotate)

    def shift_down(self, rotate=False):
        """
        Shift all pixels down

        :param rotate: (Optional) Rotate the shifted pixels to top (default=False)

        This example shifts 2 pixels down

        .. code-block:: python

            import time
            from adafruit_featherwing import dotstar_featherwing

            dotstar = dotstar_featherwing.DotStarFeatherWing()

            # Draw Red and Green Pixels
            dotstar[5, 3] = (255, 0, 0)
            dotstar[6, 3] = (0, 255, 0)

            # Rotate it off the screen
            for i in range(0, dotstar.rows - 1):
                dotstar.shift_down(True)
                time.sleep(.1)

            time.sleep(1)
            # Shift it off the screen
            for i in range(0, dotstar.rows - 1):
                dotstar.shift_down()
                time.sleep(.1)

        """
        super()._shift_down(rotate)

    @property
    def auto_write(self):
        """
        Whether or not we are automatically updating
        If set to false, be sure to call show() to update

        This lights DotStars with and without auto_write

        .. code-block:: python

            import time
            from adafruit_featherwing import dotstar_featherwing

            dotstar = dotstar_featherwing.DotStarFeatherWing()
            dotstar.fill() # Clear any lit Dotstars
            dotstar[0, 0] = (255, 255, 255) # Set White
            time.sleep(1)

            dotstar.auto_write = False
            dotstar[1, 0] = (255, 255, 255) # Set White
            time.sleep(1)
            dotstar.show() # Update the DotStars

        """
        return self._auto_write

    @auto_write.setter
    def auto_write(self, write):
        if isinstance(write, bool):
            self._auto_write = write

    @property
    def brightness(self):
        """
        Overall brightness of the display

        This example changes the brightness

        .. code-block:: python

            import time
            from adafruit_featherwing import dotstar_featherwing

            dotstar = dotstar_featherwing.DotStarFeatherWing()
            dotstar.brightness = 0
            dotstar.fill(0xFFFFFF)
            for i in range(0, 6):
                dotstar.brightness = (i / 10)
                time.sleep(.2)

            dotstar.brightness = 0.3

        """
        return self._matrix.brightness

    @brightness.setter
    def brightness(self, brightness):
        self._matrix.brightness = min(max(brightness, 0.0), 1.0)
        self._update()
