from .base_device import BaseDevice

class Common(BaseDevice):
    def __init__(self, topic, pins):
        super().__init__(topic)

        self.dht = 0 #self.dht = dht.DHT22(machine.Pin(pins['dht22']))
        self.sunligh = 0
        self.reservoir = 0

    @property
    def status(self):
        #        self.dht.measure()
        #        temp, humidity = self.temperature(), self.humidity()
        return self.to_json({'temp': 0, 'humidity': 0, 'sunlight': 0, 'reservoir_alert': 0, 'ts': self.time()})
