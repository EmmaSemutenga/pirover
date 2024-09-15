# working
# Testing the git pull

from gpiozero import DistanceSensor, Robot
from rpi_lcd import LCD
from time import sleep

# first run i2cdetect -y 1
# in terminal to determine actual address to unsert below
lcd = LCD(address=0x27)
sensor = DistanceSensor(24, 23)
robot = Robot(left=(27, 22), right=(19, 26))
lcd.text(f'Welcome to Bits Rover m', 1)

while True:
    # print('Distance to nearest object is', sensor.distance, 'm')
    lcd.text(f'{sensor.distance} m', 1)
    sleep(1)
    while sensor.distance <= 0.5:
        # print('Distance to nearest object is', sensor.distance, 'm')
        # print(type(sensor.distance))
        lcd.text(f'{round(sensor.distance,2)} m too close, please stay away', 1)
        robot.forward(speed=0.5)
        sleep(5)
        robot.stop()
        