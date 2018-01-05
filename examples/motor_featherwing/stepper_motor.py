from adafruit_featherwing import motor_featherwing

wing = motor_featherwing.MotorFeatherWing()

for i in range(100):
    wing.stepper2.onestep()
