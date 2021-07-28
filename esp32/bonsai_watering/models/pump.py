import ujson
from machine import Pin

class Pump:
    def __init__(self, pin):
        self.pin = Pin(pin, Pin.OUT)
        self._pin_num = pin

    @property
    def status(self):
        return self.pin.value()

    @status.setter
    def status(self, value):
        self.pin.value(value)

    def __repr__(self):
        #return '{}(pin={}, status={})'.format(self.__class__.__name__, self._pin_num, self.status)
        return ujson.dumps({'pin': self._pin_num, 'status': self.status})
