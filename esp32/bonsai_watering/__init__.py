import time

import MicroWebSrv2 as mws2

from bonsai_watering.models import Logger, Pump, Scheduler

""" create package instances"""
logger = Logger()
server = mws2.MicroWebSrv2()
pump = Pump(pin=23)
scheduler = Scheduler()

def create_application():
    """ main function and entry point to the package """

    """ register web routes """
    #from bonsai_watering.controllers import get_pump, post_pump, get_pump_schedule, post_pump_schedule, get_time, post_time
    import bonsai_watering.controllers as controllers

    mws2.RegisterRoute(controllers.get_pump, mws2.GET, '/pump')
    mws2.RegisterRoute(controllers.post_pump, mws2.POST, '/pump')

    mws2.RegisterRoute(controllers.get_pump_schedule, mws2.GET, '/pump/schedule')
    mws2.RegisterRoute(controllers.post_pump_schedule, mws2.POST, '/pump/schedule')

    mws2.RegisterRoute(controllers.get_time, mws2.GET, '/time')
    mws2.RegisterRoute(controllers.post_time, mws2.POST, '/time')

    mws2.RegisterRoute(controllers.get_logs, mws2.GET, '/logs')

    """ schedule jobs """
    from bonsai_watering.jobs import water_plants

    scheduler.schedule(job=water_plants, at='07:00', pump=pump, duration=40)
    scheduler.schedule(job=water_plants, at='16:00', pump=pump, duration=20)
    scheduler.schedule(job=water_plants, at='20:00', pump=pump, duration=20)

    """ set up web server"""
    server.SetEmbeddedConfig()
    """ start web server """
    server.StartManaged()

    """ main program loop until keyboard interrupt """
    try:
        while server.IsRunning:
            scheduler.run_scheduled()
            time.sleep(25)
    except KeyboardInterrupt:
        server.Stop()
        server.Log('Byee', server.DEBUG)
