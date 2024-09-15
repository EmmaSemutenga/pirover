from gpiozero import Robot
from time import sleep

robot = Robot(left=(27, 22), right=(19, 26))

for i in range(4):
    robot.forward(speed=0.5)
    sleep(10)
    robot.right(speed=0.5)
    sleep(1)