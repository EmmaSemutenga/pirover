# working
from rpi_lcd import LCD
from time import sleep

# first run i2cdetect -y 1
# in terminal to determine actual address to unsert below

lcd = LCD(address=0x27)

lcd.text('Hello World!', 1)
sleep(5)
lcd.text('Raspberry Pi', 2)
sleep(1)
lcd.text('is really', 1, 'center')
sleep(1)
lcd.text('awesome', 2, 'right')

sleep(5)
lcd.clear()