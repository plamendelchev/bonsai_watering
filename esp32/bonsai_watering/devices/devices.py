import esp32, gc, os
from machine import Signal, Pin, ADC #, dht

from .base_device import BaseDevice

class Plant(BaseDevice):
    def __init__(self, topic, pins):
        super().__init__(topic)

        self.pump = Signal(pins['pump'], Pin.OUT)
        #        self.sprayer = Signal(pins['spayer'], Pin.OUT)
        #        self.moisture = self._setup_adc(pin=pins['moisture'])

    def _setup_adc(self, pin):
        adc = ADC(Pin(pin))
        adc.atten(ADC.ATTN_11DB)
        adc.width(ADC.WIDTH_12BIT)
        return adc

    @property
    def status(self):
        #        return {'pump': self.pump.value(), 'sprayer': self.sprayer.value(), 'moisture': self.moisture.read(), **self.get_time()}
        return self.to_json({'pump': self.pump.value(), 'sprayer': 0, 'moisture': 0, 'ts': self.time()})

    ''' NEED TO IMPLEMENT THIS '''
    @status.setter
    def status(self, value):
        pass

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

class BoardStats(BaseDevice):
    @property
    def status(self):
        temp = self.temp()
        memory_usage = self.memory()
        unix_ts = self.time()
        return self.to_json({'raw_temp': temp, 'mem_alloc': memory_usage[0], 'mem_free': memory_usage[1], 'mem_total': memory_usage[2], 'ts': unix_ts})

    def temp(self):
        temp = (esp32.raw_temperature() - 32) / 1.8
        return '{:.1f}'.format(temp)

    def memory(self):
        ''' return values in KB '''
        gc.collect()
        free, alloc = (gc.mem_free() / 1024), (gc.mem_alloc() / 1024)
        return (alloc, free, free + alloc)

    def storage(self):
        ''' returns values in MB '''
        storage = os.statvfs('/')
        available = float('{:.3f}'.format((storage[0] * storage[3]) / 1048576))
        total = float('{:.3f}'.format((storage[0] * storage[2]) / 1048576))
        return used, available, total - available
