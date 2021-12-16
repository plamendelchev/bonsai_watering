from machine import Pin
import ujson

class Pump:
    def __init__(self, name, pin, topic):
        self.name = name
        self._pin = Pin(pin, Pin.OUT)
        self._pin_num = pin
        self.topic = topic

    @property
    def pin(self):
        return self._pin_num

    @property
    def data(self):
        return ujson.dumps({'name': self.name, 'type': self.__class__.__name__, 'pin': self.pin, 'status': self.status})

    @property
    def status(self):
        return self._pin.value()

    @status.setter
    def status(self, value):
        self._pin.value(value)

    def __repr__(self):
        return repr({'name': self.name, 'type': self.__class__.__name__, 'pin': self.pin, 'status': self.status, 'topic': self.topic})
