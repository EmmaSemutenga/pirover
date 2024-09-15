# working
# Testing the git pull

from gpiozero import DistanceSensor, Robot
from rpi_lcd import LCD
from time import sleep

# first run i2cdetect -y 1
# in terminal to determine actual address to unsert below
lcd = LCD(address=0x3c)
lcd.text(f'Welcome to Bits Rover m', 1)
