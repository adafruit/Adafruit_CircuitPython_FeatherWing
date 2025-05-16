# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Example to print out the voltage and current using the INA219"""

import time

from adafruit_featherwing import ina219_featherwing

INA219 = ina219_featherwing.INA219FeatherWing()

while True:
    print(f"Bus Voltage:   {INA219.bus_voltage} V")
    print(f"Shunt Voltage: {INA219.shunt_voltage} V")
    print(f"Voltage:       {INA219.voltage} V")
    print(f"Current:       {INA219.current} mA")
    print("")
    time.sleep(0.5)
