from machine import Pin

class Pump:
    def __init__(self, pin):
        self.pin = Pin(pin, Pin.OUT)

    @property
    def status(self):
        #return {'status': self.pin.value()}
        return self.pin.value()

    @status.setter
    def status(self, value):
        self.pin.value(value)

    def __repr__(self):
        return '{}(pin={}, status={})'.format(self.__class__.__name__, self.pin, self.status)
