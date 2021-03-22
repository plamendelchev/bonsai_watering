from MicroWebSrv2 import *
from machine import Pin
import time

@WebRoute(GET, '/pump')
def get_pump(mws2, request):
    request.Response.ReturnOkJSON({'status': pin.value()})

@WebRoute(POST, '/pump')
def post_pump(msw2, request):
    data = request.GetPostedJSONObject()
    try:
        action = data['action']
    except:
        request.Response.ReturnBadRequest()
        return

    pin.value(int(action))
    request.Response.ReturnOkJSON({'status': pin.value()})


pin = Pin(23, Pin.OUT)
mws2 = MicroWebSrv2()
mws2.SetEmbeddedConfig()
mws2.StartManaged()

# Main program loop until keyboard interrupt
try:
    while mws2.IsRunning:
        sleep(1)
except KeyboardInterrupt:
    pass

# End
print()
mws2.Stop()
print('Bye')
print()
