# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This example will allow you to set the date and time
and then loop through and display the current time
"""

import time

from adafruit_featherwing import rtc_featherwing

days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

# Create the RTC instance:
rtc = rtc_featherwing.RTCFeatherWing()

if True:  # Change this to True to set the date and time
    rtc.set_time(13, 34)  # Set the time (seconds are optional)
    print(rtc.now)
    rtc.set_date(16, 1, 2016)  # Set the date
    print(rtc.now)
    rtc.year = 2019  # Set just the Year
    print(rtc.now)
    rtc.month = 2  # Set Just the Month
    print(rtc.now)
    rtc.hour = 16  # Set just the hour
    print(rtc.now)
    rtc.weekday = 6  # Set just the day of the week (Sunday = 0)
    print(rtc.now)
    rtc.unixtime = 1550335257  # Or set the date and time with a unix timestamp

# Main loop:
while True:
    now = rtc.now
    print(f"The date is {days[now.weekday]} {now.day}/{now.month}/{now.year}")
    print(f"The time is {now.hour}:{now.minute:02}:{now.second:02}")
    print(f"The UNIX timestamp is {rtc.unixtime}")
    print(f"The number of days in the current month is {rtc.get_month_days()}")
    if rtc.is_leap_year():
        print("This year is a leap year")
    else:
        print("This year is not a leap year")
    time.sleep(1)  # wait a second
