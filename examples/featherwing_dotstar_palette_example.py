# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This creates a palette of colors, draws a pattern and
rotates through the palette creating a moving rainbow.
"""

from math import cos, radians, sin, sqrt

from adafruit_featherwing import dotstar_featherwing

dotstar = dotstar_featherwing.DotStarFeatherWing()


# Remap the calculated rotation to 0 - 255
def remap(vector):
    return int(((255 * vector + 85) * 0.75) + 0.5)


# Calculate the Hue rotation starting with Red as 0 degrees
def rotate(degrees):
    cosA = cos(radians(degrees))
    sinA = sin(radians(degrees))
    red = cosA + (1.0 - cosA) / 3.0
    green = 1.0 / 3.0 * (1.0 - cosA) + sqrt(1.0 / 3.0) * sinA
    blue = 1.0 / 3.0 * (1.0 - cosA) - sqrt(1.0 / 3.0) * sinA
    return (remap(red), remap(green), remap(blue))


palette = []
pixels = []

# Generate a rainbow palette
for degree in range(0, 360):
    color = rotate(degree)
    palette.append(color[0] << 16 | color[1] << 8 | color[2])

# Create the Pattern
for y in range(0, dotstar.rows):
    for x in range(0, dotstar.columns):
        pixels.append(x * 30 + y * -30)

# Clear the screen
dotstar.fill()

# Start the Animation
dotstar.auto_write = False
while True:
    for color in range(0, 360, 10):
        for index in range(0, dotstar.rows * dotstar.columns):
            palette_index = pixels[index] + color
            if palette_index >= 360:
                palette_index -= 360
            elif palette_index < 0:
                palette_index += 360
            dotstar[index] = palette[palette_index]
        dotstar.show()
