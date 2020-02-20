import machine
import dht22
import time

LED_PIN = 2  # D4
DEBUG_PIN = 14 # D5
DHT22_PIN = 4  # D2

LOG_INTERVAL = 600

def blink(time_in_sec):
    led = machine.Pin(LED_PIN, machine.Pin.OUT)
    for i in range(int(time_in_sec*5)):
        led.on()
        time.sleep(0.1)
        led.off()
        time.sleep(0.1)
    led.on()

def show_error():
    led = machine.Pin(LED_PIN, machine.Pin.OUT)
    for i in range(3):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)
    led.on()


def is_debug():
    debug = machine.Pin(config.DEBUG_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    if debug.value() == 0:
        print('Debug mode detected.')
        return True
    return False


def deepsleep():
    print('Going into deepsleep for {seconds} seconds...'.format(
        seconds=LOG_INTERVAL))
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
    rtc.alarm(rtc.ALARM0, LOG_INTERVAL * 1000)
    machine.deepsleep()


# get the temps
def get_temperature_and_humidity():
    dht22 = dht.DHT22(machine.Pin(config.DHT22_PIN))
    dht22.measure()
    return dht22.temperature(), dht22.humidity()
