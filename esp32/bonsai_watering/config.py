from machine import Pin
from mqtt_as import config

# mqtt_as settings
config.update({
    'server': '192.168.0.200',
    'port': 8888,
    'ssid': 'gosho',
    'wifi_pw': 'P1am3n4o97'
})

# Light board LEDs
def ledfunc(pin):
    pin = pin
    def func(v):
        pin(not v)  # Active low on ESP8266
    return func

wifi_led = ledfunc(Pin(0, Pin.OUT, value = 0))  # Red LED for WiFi fail/not ready yet
blue_led = ledfunc(Pin(2, Pin.OUT, value = 1))  # Message received
