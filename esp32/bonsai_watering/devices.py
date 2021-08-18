from bonsai_watering import models

pump = models.Pump(pin=23)

devices = {'pump': pump}

def get(device_name):
    return devices[device_name]
