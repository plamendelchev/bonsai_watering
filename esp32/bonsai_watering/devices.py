from bonsai_watering import models

pump = models.Pump(name='pump', pin=23)
pump2 = models.Pump(name='pump2', pin=25)

devices = [pump, pump2]

def get(device_name):
    return next(device for device in devices if device.name == device_name)
