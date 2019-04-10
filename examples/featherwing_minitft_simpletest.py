"""
This example display a CircuitPython console and
print which button that is being pressed if any

Note: This relies on displayio which is only widely
available on CircuitPython 4.0 Beta 5 and later
"""
import time
from adafruit_featherwing import minitft_featherwing

minitft = minitft_featherwing.MiniTFTFeatherWing()

while True:
    if minitft.button_right:
        print("Button RIGHT!")

    if minitft.button_down:
        print("Button DOWN!")

    if minitft.button_left:
        print("Button LEFT!")

    if minitft.button_up:
        print("Button UP!")

    if minitft.button_select:
        print("Button SELECT!")

    if minitft.button_a:
        print("Button A!")

    if minitft.button_b:
        print("Button B!")

    time.sleep(.01)
