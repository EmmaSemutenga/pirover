# working

from board import SCL, SDA
import busio
from oled_text import OledText
from time import sleep

i2c = busio.I2C(SCL, SDA)

# Create the display, pass its pixel dimensions
oled = OledText(i2c, 128, 32)

for i in range(3):
    oled.text(f"IN {i+1}", 1)
    sleep(2)

# Write to the oled
oled.text("Welcome", 1)  # Line 1
oled.text("To", 2)  # Line 2
oled.text("Kampabits", 3)  # Line 2
sleep(4)
oled.clear()