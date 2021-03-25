from MicroWebSrv2 import MicroWebSrv2, WebRoute, GET, POST, sleep
from app import Pump

pump = Pump(pin=23)
mws2 = MicroWebSrv2()

@WebRoute(GET, '/pump')
def get_pump(mws2, request):
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

    request.Response.ReturnOkJSON(pump.status)

def start_app():
    mws2.SetEmbeddedConfig()
    mws2.StartManaged()

    # Main program loop until keyboard interrupt
    try:
        while mws2.IsRunning:
            sleep(1)
    except KeyboardInterrupt:
        pass

    # End
    mws2.Stop()
    print('Bye')
