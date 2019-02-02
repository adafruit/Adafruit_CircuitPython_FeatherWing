"""
This example changes the screen different colors
and then draws random pixels at random locations
"""

from time import sleep
import random
from adafruit_featherwing import dotstar_featherwing

dotstar = dotstar_featherwing.DotStarFeatherWing()

# HELPERS
# a random color 0 -> 224
def random_color():
    return random.randrange(0, 8) * 32

for i in range(0, 15):
    dotstar.fill((random_color(), random_color(), random_color()))
    sleep(.2)

# MAIN LOOP
while True:
    # Fill screen with a random color
    x = random.randrange(0, dotstar.columns)
    y = random.randrange(0, dotstar.rows)
    dotstar[x, y] = (random_color(), random_color(), random_color())
    sleep(.1)
