from adafruit_featherwing import ina219_featherwing
import time

ina219 = ina219_featherwing.INA219FeatherWing()

while True:
    print("Bus Voltage:   {} V".format(ina219.bus_voltage))
    print("Shunt Voltage: {} V".format(ina219.shunt_voltage))
    print("Voltage:       {} V".format(ina219.voltage))
    print("Current:       {} mA".format(ina219.current))
    print("")
    time.sleep(0.5)
