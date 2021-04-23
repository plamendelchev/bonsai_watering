import time

from bonsai_watering.common import pump, server, scheduler
import bonsai_watering.controllers

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
    server.SetEmbeddedConfig()
    server.StartManaged()
