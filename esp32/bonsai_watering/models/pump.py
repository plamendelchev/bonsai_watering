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

    @property
    def all_attributes(self):
        return {'pin': self._pin_num, 'status': self.status}

    def __repr__(self):
        return {'pin': self._pin_num, 'status': self.status}
