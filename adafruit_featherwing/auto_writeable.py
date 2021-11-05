# SPDX-FileCopyrightText: 2021 Tim Cocks for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_featherwing.auto_writeable`
====================================================

Superclass for the helpers pixelmatrix and matrix_featherwing

* Author(s): Tim Cocks
"""


class AutoWriteable:
    """Superclass for matrix_featherwing and pixelmatrix."""

    def __init__(self):
        self._auto_write = True

    @property
    def auto_write(self):
        """
        Whether or not we are automatically updating
        If set to false, be sure to call show() to update
        """
        return self._auto_write

    @auto_write.setter
    def auto_write(self, write: bool):
        if isinstance(write, bool):
            self._auto_write = write
