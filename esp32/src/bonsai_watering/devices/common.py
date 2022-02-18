import dht
import machine
from bh1750 import BH1750
from .base_device import BaseDevice

class Common(BaseDevice):
    def __init__(self, topic, pins):
        super().__init__(topic)
        self._dht = dht.DHT22(machine.Pin(pins['dht22']))
        self._bh1750 = BH1750(machine.I2C(
            scl = machine.Pin(pins['light'][0]),
            sda = machine.Pin(pins['light'][1]),
            freq = 400000
        ))
        # self.reservoir = self.pins['reservoir']

    @property
    def dht(self):
        self._dht.measure()
        return self._dht.temperature(), self._dht.humidity()

    @property
    def luminance(self):
        return self._bh1750.luminance(BH1750.ONCE_HIRES_2)

    @property
    def status(self):
        temp, humidity = self.dht
        luminance = self.luminance
        return self.to_json({'temp': temp, 'humidity': humidity, 'sunlight': luminance, 'reservoir_alert': 0, 'ts': self.time()})
