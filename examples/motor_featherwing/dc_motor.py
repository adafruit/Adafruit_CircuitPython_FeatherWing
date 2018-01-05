import time
from adafruit_featherwing import motor_featherwing

wing = motor_featherwing.MotorFeatherWing()

wing.motor4.throttle = 1.0
time.sleep(0.2)

wing.motor4.throttle = 0
