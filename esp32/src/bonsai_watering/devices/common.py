import dht
import machine
from .base_device import BaseDevice

class Common(BaseDevice):
    def __init__(self, topic, pins):
        super().__init__(topic)
        self.dht = dht.DHT22(machine.Pin(pins['dht22']))
        # self.sunligh = self.pins['sunlight']
        # self.reservoir = self.pins['reservoir']

    @property
    def status(self):
        self.dht.measure()
        temp, humidity = self.dht.temperature(), self.dht.humidity()
        return self.to_json({'temp': temp, 'humidity': humidity, 'sunlight': 0, 'reservoir_alert': 0, 'ts': self.time()})
