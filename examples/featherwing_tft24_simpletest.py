import board
from adafruit_featherwing import tft_featherwing_24

tft_featherwing = tft_featherwing_24.TFTFeatherWing24()

f = open("/sd/tft_featherwing.txt", "w")
f.write("Blinka\nTFT 2.4\" FeatherWing")
f.close()

f = open("/sd/tft_featherwing.txt", "r")
print(f.read())
f.close()

while True:
    if not tft_featherwing.touchscreen.buffer_empty:
        print(tft_featherwing.touchscreen.read_data())
