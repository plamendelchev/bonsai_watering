import esp
import gc
import micropython
from mqtt_as import config

esp.osdebug(None)
gc.enable()
micropython.alloc_emergency_exception_buf(100)

wifi_plovdiv = {'ssid': 'gosho', 'password': 'P1am3n4o97'}
wifi_dgrad = {'ssid': 'Tech_D3943340', 'password': 'SBKMVXXQ'}

# mqtt_as settings
config.update({
    'server': '192.168.0.200',
    'port': 1883,
    'user': 'esp32',
    'password': '5cfN!VT9]mM,@vAr',
    'ssid': wifi_plovdiv['ssid'],
    'wifi_pw': wifi_plovdiv['password']
})

gc.collect()
