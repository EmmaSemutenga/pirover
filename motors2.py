from gpiozero import Motor
from time import sleep

motor = Motor(forward=27, backward=22)

while True:
    motor.forward(speed=0.9)
    sleep(5)
    # motor.backward(speed=0.4)
    # sleep(5)



# from gpiozero import LED 

# from time import sleep

# motor_lockwise= LED(22)
# motor_anticlockwise = LED(27)
# motor_clockwise_2 = LED(26)
# motor_anticlockwise_2 = LED(19)


# motor_lockwise.on()
# motor_clockwise_2.on()
# motor_anticlockwise.off()
# motor_anticlockwise_2.off()
# sleep(10)
# motor_lockwise.off()
# motor_clockwise_2.off()
# motor_anticlockwise.on()
# motor_anticlockwise_2.on()
# sleep(10)