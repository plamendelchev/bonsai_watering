from MicroWebSrv2 import MicroWebSrv2, RegisterRoute, GET, POST
from time import sleep
from .models import Pump

pump = Pump(pin=23)
mws2 = MicroWebSrv2()

def create_application():
    # Set up webserver
    initialize_server(mws2)

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

def initialize_server(mws2):
    from .controllers import get_pump, post_pump

    mws2.SetEmbeddedConfig()

    RegisterRoute(get_pump, GET, '/pump')
    RegisterRoute(post_pump, POST, '/pump')
