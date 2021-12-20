from machine import Pin
import esp32

class Pump:
    def __init__(self, pin, topic):
        self._pin = Pin(pin, Pin.OUT)
        self._pin_num = pin
        self.topic = topic

    @property
    def pin(self):
        return self._pin_num

    @property
    def status(self):
        return self._pin.value()

    @status.setter
    def status(self, value):
        try:
            self._pin.value(int(value))
        except ValueError:
            pass

    def __repr__(self):
        return repr({'type': self.__class__.__name__, 'pin': self.pin, 'status': self.status, 'topic': self.topic})

class TemperatureSensor:
    def __init__(self, topic):
        self.topic = topic

    @property
    def status(self):
        temp_f = esp32.raw_temperature()
        temp_c = (temp_f - 32) / 1.8
        return '{:.1f}'.format(temp_c)

    def __repr__(self):
        return repr({'type': self.__class__.__name__, 'status': self.status, 'topic': self.topic})
