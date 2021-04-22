import time

import MicroWebSrv2 as mws2

from .scheduler import Scheduler
from app.models import Pump


pump = Pump(pin=23)
scheduler = Scheduler()
server = mws2.MicroWebSrv2()

def create_application():
    # 
    schedule_jobs(scheduler)
    # Set up and start webserver
    initialize_server(server)

    # Main program loop until keyboard interrupt
    try:
        while server.IsRunning:
            time.sleep(1)
            scheduler.run_scheduled()
    except KeyboardInterrupt:
        server.Stop()
        print('Bye')

def schedule_jobs(scheduler):
    def water_plants():
        pump.status = 1
        time.sleep(8)
        pump.status = 0

    scheduler.schedule(water_plants, at='12:44')

def initialize_server(server):
    from app.controllers import get_pump, post_pump

    mws2.RegisterRoute(get_pump, mws2.GET, '/pump')
    mws2.RegisterRoute(post_pump, mws2.POST, '/pump')

    server.SetEmbeddedConfig()
    server.StartManaged()
