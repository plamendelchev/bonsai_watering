from MicroWebSrv2 import MicroWebSrv2, RegisterRoute, GET, POST
from time import sleep
from app.models import Pump

pump = Pump(pin=23)
mws2 = MicroWebSrv2()

def create_application():

    # Set up webserver
    initialize_server(mws2)

    # Start webserver
    mws2.StartManaged()

    # Main program loop until keyboard interrupt
    try:
        while mws2.IsRunning:
            sleep(1)
    except KeyboardInterrupt:
        mws2.Stop()
        print('Bye')

def initialize_server(mws2):
    from app.controllers import get_pump, post_pump

    mws2.SetEmbeddedConfig()

    RegisterRoute(get_pump, GET, '/pump')
    RegisterRoute(post_pump, POST, '/pump')
