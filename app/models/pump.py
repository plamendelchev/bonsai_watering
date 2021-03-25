from machine import Pin

class Pump:
    def __init__(self, pin):
        self._pin = Pin(pin, Pin.OUT)

    @property
    def pin(self):
        return self._pin.id

    @property
    def status(self):
        return {'status': self._pin.value()}

    @status.setter
    def status(self, value):
        self._pin.value(value)
