from MicroWebSrv2 import *
from app import Pump
#from machine import Pin
import time

#pin = Pin(23, Pin.OUT)
pump = Pump(pin=23)

mws2 = MicroWebSrv2()
mws2.SetEmbeddedConfig()
mws2.StartManaged()

@WebRoute(GET, '/pump')
def get_pump(mws2, request):
    #request.Response.ReturnOkJSON({'status': pin.value()})
    request.Response.ReturnOkJSON(pump.status)

@WebRoute(POST, '/pump')
def post_pump(msw2, request):
    data = request.GetPostedJSONObject()
    try:
        status = data['status']
    except KeyError:
        request.Response.ReturnBadRequest()
        return

    pump.status = int(status)

    #request.Response.ReturnOkJSON({'status': pin.value()})
    request.Response.ReturnOkJSON(pump.status)

# Main program loop until keyboard interrupt
try:
    while mws2.IsRunning:
        sleep(1)
except KeyboardInterrupt:
    pass

# End
mws2.Stop()
print('Bye')
