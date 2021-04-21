from time import sleep

import MicroWebSrv2 as mws2

from app.models import Pump

pump = Pump(pin=23)
server = mws2.MicroWebSrv2()

def create_application():
    # Set up and start webserver
    initialize_server(server)

    # Main program loop until keyboard interrupt
    try:
        while server.IsRunning:
            pass
    except KeyboardInterrupt:
        server.Stop()
        print('Bye')

def initialize_server(server):
    from app.controllers import get_pump, post_pump

    mws2.RegisterRoute(get_pump, mws2.GET, '/pump')
    mws2.RegisterRoute(post_pump, mws2.POST, '/pump')

    server.SetEmbeddedConfig()
    server.StartManaged()
