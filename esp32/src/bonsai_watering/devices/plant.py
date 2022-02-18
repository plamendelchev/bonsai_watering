import json
from machine import Signal, Pin, ADC
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
        return self.to_json({'pump': self.pump.value(), 'sprayer': 0, 'moisture': 0, 'ts': self.time()})

    '''
    bonsai/set/plants/<name>
    value:
        {"pump": 1}
        {"pump": 0, "sprayer": 1}
    '''
    @status.setter
    def status(self, payload):
        try:
            data = json.loads(payload)
        except ValueError:
            pass
        else:
            for key, value in data.items():
                try:
                    attr = getattr(self, key)
                    attr.value(int(value))
                except (AttributeError, ValueError):
                    continue
