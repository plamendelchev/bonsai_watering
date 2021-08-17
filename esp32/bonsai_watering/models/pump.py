from machine import Pin

class Pump:
    def __init__(self, pin):
        self._pin = Pin(pin, Pin.OUT)
        self._pin_num = pin

    @property
    def pin(self):
        return self._pin_num

    @property
    def status(self):
        return self._pin.value()

    @status.setter
    def status(self, value):
        self._pin.value(value)

    @property
    def all_attributes(self):
        return {'pin': self.pin, 'status': self.status}

    def __repr__(self):
        return str({'pin': self.pin, 'status': self.status})
