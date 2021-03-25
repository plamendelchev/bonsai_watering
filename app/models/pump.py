from machine import Pin

class Pump:
    def __init__(self, pin):
        self._pin = Pin(pin, Pin.OUT)

    @property
    def pin(self):
        return self._pin.id

    @property
    def status(self):
        return self._pin.value()

    @status.setter(self, value):
        self._pin.value(value)
