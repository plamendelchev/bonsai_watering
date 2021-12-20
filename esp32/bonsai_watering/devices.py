from bonsai_watering import models

pump = models.Pump(name='pump', pin=23)

devices = [pump]

def get(device_name):
    return next(device for device in devices if device.name == device_name)
