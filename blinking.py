import machine
import time

LED_PIN = 2  # D4
LED2_PIN = 16  # D0

def blink(time_in_sec):
    led = machine.Pin(LED_PIN, machine.Pin.OUT)
    led2 = machine.Pin(LED2_PIN, machine.Pin.OUT)
#   button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    for i in range(int(time_in_sec*5)):
        led.on()
        led2.off()
        time.sleep(0.1)
        led.off()
        led2.on()
        time.sleep(0.1)
    led.on()
    led2.on()
