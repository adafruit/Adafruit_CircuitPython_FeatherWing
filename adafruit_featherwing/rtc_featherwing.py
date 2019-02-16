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
`adafruit_featherwing.rtc_featherwing`
====================================================

Helper for using the `DS3231 Precision RTC FeatherWing
<https://www.adafruit.com/product/3028>`_.

* Author(s): Melissa LeBlanc-Williams
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_FeatherWing.git"

import time
from collections import namedtuple
from adafruit_featherwing import shared
import adafruit_ds3231

"""
Other things
Make it 12/24 hour format settable
Have the return values format appropriately
Maybe set based on format
Add all the parameters for RTD
Add some examples for the functions
"""

class RTCFeatherWing:
    """Class representing an `DS3231 Precision RTC FeatherWing
       <https://www.adafruit.com/product/3028>`_.

       Automatically uses the feather's I2C bus."""
    def __init__(self):
        self._rtc = adafruit_ds3231.DS3231(shared.I2C_BUS)

    def __setitem__(self, index, value):
        """
        Allow updates using setitem if that makes it easier
        """
        self._set_time_value(self, index, value)

    def __getitem__(self, index):
        """
        Allow retrievals using getitem if that makes it easier
        """
        return self._get_time_value(self, index)

    def _set_time_value(self, unit, value):
        """
        Set just the specific unit of time
        """
        date = self._get_now()
        if unit in date:
            date[unit] = value
        else:
            raise ValueError('The specified unit of time is invalid')

        self._rtc.datetime = self._encode(date)

    def _get_time_value(self, unit):
        """
        Get just the specific unit of time
        """
        time = self._get_now()
        if unit in time:
            return time[unit]
        else:
            raise ValueError('The specified unit of time is invalid')

    def _get_now(self):
        """
        Return the current date and time in a nice updatable dictionary
        """
        now = self._rtc.datetime
        MyStruct = namedtuple("MyStruct", "field1 field2 field3")
        return {'second': now.tm_sec, 'minute': now.tm_min, 'hour': now.tm_hour, 'day': now.tm_mday,
                'month': now.tm_mon, 'year': now.tm_year, 'weekday': now.tm_wday}

    def _encode(self, date):
        """
        Encode the updatable dictionary back into a time struct
        """
        now = self._rtc.datetime
        return time.struct_time((date['year'], date['month'], date['day'], date['hour'],
                                 date['minute'], date['second'], date['weekday'], now.tm_yday,
                                 now.tm_isdst))

#REMOVE ME          20                  40                  60                  80                  100
    def set_time(self, hour, minute, second):
        """
        Set the time only

        :param int hour: The hour we want to set the time to
        :param int minute: The minute we want to set the time to
        :param int second: The second we want to set the time to
        """
        now = self._get_now()
        now['hour'] = hour
        now['minute'] = minute
        now['second'] = second
        self._rtc.datetime = self._encode(now)

    def set_date(self, day, month, year):
        """
        Set the date only

        :param int day: The day we want to set the date to
        :param int month: The month we want to set the date to
        :param int year: The year we want to set the date to
        """
        now = self._get_now()
        now['day'] = day
        now['month'] = month
        now['year'] = year
        self._rtc.datetime = self._encode(now)

    @property
    def datetime(self):
        """
        Passthru property to the ds3231 library for compatibility
        """
        return self._rtc.datetime

    @datetime.setter
    def datetime(self, datetime):
        self._rtc.datetime = datetime

    @property
    def year(self):
        """
        The Current Year
        """
        return self._get_time_value('year')

    @year.setter
    def year(self, year):
        self._set_time_value('year', year)

    @property
    def month(self):
        """
        The Current Month
        """
        return self._get_time_value('month')

    @month.setter
    def month(self, month):
        self._set_time_value('month', month)

    @property
    def day(self):
        """
        The Current Day
        """
        return self._get_time_value('day')

    @day.setter
    def day(self, day):
        self._set_time_value('day', day)

    @property
    def hour(self):
        """
        The Current Hour
        """
        return self._get_time_value('hour')

    @hour.setter
    def hour(self, hour):
        self._set_time_value('hour', hour)

    @property
    def minute(self):
        """
        The Current Minute
        """
        return self._get_time_value('minute')

    @minute.setter
    def minute(self, minute):
        self._set_time_value('minute', minute)

    @property
    def second(self):
        """
        The Current Second
        """
        return self._get_time_value('second')

    @second.setter
    def second(self, second):
        self._set_time_value('second', second)

    @property
    def weekday(self):
        """
        The Current Day of the Week Value (0-6) where Sunday is 0
        """
        return self._get_time_value('weekday')

    @weekday.setter
    def weekday(self, weekday):
        self._set_time_value('weekday', weekday)

    @property
    def weekday_name(self):
        """
        The Name for the Current Day of the Week (Read Only)
        """
        days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
        return days[self._get_time_value('weekday')]

    @property
    def now(self):
        """
        The Current Date and Time in Named Tuple Style
        """
        DateTime = namedtuple("DateTime", "second minute hour day month year weekday")
        return DateTime(**self._get_now())
