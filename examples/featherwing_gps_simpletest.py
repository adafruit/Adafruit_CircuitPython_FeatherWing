# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This example will connect to the GPS at the default 9600 baudrate and
update once per second. Initialization is automatically handled and there
are some additional features such as MPH and KPH calculations.
"""

import time

from adafruit_featherwing import gps_featherwing

# Create a GPS featherwing instance.
gps = gps_featherwing.GPSFeatherWing()

# Main loop runs forever printing the location, etc. every second.
last_print = time.monotonic()
while True:
    # Make sure to call gps.update() every loop iteration and at least twice
    # as fast as data comes from the GPS unit (usually every second).
    # This returns a bool that's true if it parsed new data (you can ignore it
    # though if you don't care and instead look at the has_fix property).
    gps.update()
    # Every second print out current location details if there's a fix.
    current = time.monotonic()
    if current - last_print >= 1.0:
        last_print = current
        if not gps.has_fix:
            # Try again if we don't have a fix yet.
            print("Waiting for fix...")
            continue
        # Print out details about the fix like location, date, etc.
        print("=" * 40)  # Print a separator line.
        print(
            "Fix timestamp: {}/{}/{} {:02}:{:02}:{:02}".format(  # noqa: UP032
                gps.timestamp.tm_mon,  # Grab parts of the time from the
                gps.timestamp.tm_mday,  # struct_time object that holds
                gps.timestamp.tm_year,  # the fix time.  Note you might
                gps.timestamp.tm_hour,  # not get all data like year, day,
                gps.timestamp.tm_min,  # month!
                gps.timestamp.tm_sec,
            )
        )
        print(f"Latitude: {gps.latitude:.6f} degrees")
        print(f"Longitude: {gps.longitude:.6f} degrees")
        print(f"Fix quality: {gps.fix_quality}")
        # Some attributes beyond latitude, longitude and timestamp are optional
        # and might not be present.  Check if they're None before trying to use!
        if gps.satellites is not None:
            print(f"# satellites: {gps.satellites}")
        if gps.altitude is not None:
            print(f"Altitude: {gps.altitude} meters")
        if gps.speed_knots is not None:
            print(f"Speed (Knots): {gps.speed_knots} knots")
        if gps.speed_mph is not None:
            print(f"Speed (Miles Per Hour): {gps.speed_mph} MPH")
        if gps.speed_kph is not None:
            print(f"Speed (KM Per Hour): {gps.speed_kph} KPH")
        if gps.track_angle is not None:
            print(f"Track angle: {gps.track_angle} degrees")
        if gps.horizontal_dilution is not None:
            print(f"Horizontal dilution: {gps.horizontal_dilution}")
        if gps.height_geoid is not None:
            print(f"Height geo ID: {gps.height_geoid} meters")
