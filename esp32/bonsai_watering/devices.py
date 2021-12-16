from bonsai_watering import models

devices = []

def register_device(name, type, pin, pub_topic):
    device_class = getattr(models, type)
    device = device_class(name=name, pin=pin, topic=pub_topic)
    devices.append(device)
    return device

def get(device_name):
    return next(device for device in devices if device.name == device_name)
