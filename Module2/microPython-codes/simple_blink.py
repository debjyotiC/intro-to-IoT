from machine import Pin
import utime

led_pin = Pin(25, Pin.OUT)

while True:
    led_pin.value(1)
    utime.sleep(1)
    led_pin.value(0)
    utime.sleep(1)