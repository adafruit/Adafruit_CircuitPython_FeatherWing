"""This example changes the screen different colors"""

from time import sleep
import random
from adafruit_featherwing import dotstar_featherwing

dotstar = dotstar_featherwing.DotStarFeatherWing()

# HELPERS
# a random color 0 -> 224
def random_color():
    return random.randrange(0, 8) * 32

# MAIN LOOP
while True:
    # Fill screen with a random color
    dotstar.fill((random_color(), random_color(), random_color()))
    sleep(.25)
