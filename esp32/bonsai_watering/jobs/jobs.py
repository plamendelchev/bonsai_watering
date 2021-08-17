import time
from bonsai_watering import pump

def water_plants(pump, duration):
    pump.status = 1
    time.sleep(duration)
    pump.status = 0
