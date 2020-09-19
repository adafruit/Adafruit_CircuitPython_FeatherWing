"""
This example will display a CircuitPython console and
print the coordinates of touchscreen presses, as well
as keyboard events from the BBQ10 keyboard.
It will also try to write and then read a file on the
SD Card.

"""
from adafruit_featherwing import keyboard_featherwing
from bbq10keyboard import STATE_PRESS, STATE_RELEASE, STATE_LONG_PRESS

kbd_featherwing = keyboard_featherwing.KeyboardFeatherwing()

# set the neopixel on the kbd featherwing
kbd_featherwing.neopixel.brightness = 0.1
kbd_featherwing.neopixel[0] = 0x002244

try:
    f = open("/sd/tft_featherwing.txt", "w")
    f.write("Blinka\nBlackberry Q10 Keyboard")
    f.close()

    f = open("/sd/tft_featherwing.txt", "r")
    print(f.read())
    f.close()
except OSError as error:
    print("Unable to write to SD Card.")

while True:
    # print touch info
    if not kbd_featherwing.touchscreen.buffer_empty:
        print(kbd_featherwing.touchscreen.read_data())

    # print keyboard events
    key_count = kbd_featherwing.keyboard.key_count
    if key_count > 0:
        key = kbd_featherwing.keyboard.key
        state = 'pressed'
        if key[0] == STATE_LONG_PRESS:
            state = 'held down'
        elif key[0] == STATE_RELEASE:
            state = 'released'
        print("key: '%s' (dec %d, hex %02x) %s" % (key[1], ord(key[1]), ord(key[1]), state))
