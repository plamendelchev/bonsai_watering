from .devices import *
from .board_devices import *

PUMP='Pump'
B_TEMP='TemperatureSensor'
B_MEMORY='BoardMemory'
B_STORAGE='BoardStorage'
B_TIME='BoardTime'

devices = []
board_devices = []

def register_device(type, topic, **kwargs):
    device_class = globals()[type]
    device = device_class(topic=topic, **kwargs)

    if type.startswith('Board'):
        board_devices.append(device)
    else:
        devices.append(device)

    return device

def change_status(topic, message):
    device_name = topic.decode('utf-8').split('/')[-1]

    for device in devices:
        if device.topic.endswith(device_name):
            device.status = message.decode('utf-8')
            break
