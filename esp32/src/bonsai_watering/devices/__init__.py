from .plant import Plant
from .common import Common
from .board_stats import BoardStats

PLANT='Plant'
COMMON='Common'
BOARD_STATS='BoardStats'

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
    device_name = topic.decode().split('/')[-1]

    for device in devices:
        if device.topic.endswith(device_name):
            print(f'Changing status of {device_name}')
            device.status = message.decode()
            break
