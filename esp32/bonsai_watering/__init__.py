import time

import MicroWebSrv2 as mws2

from bonsai_watering.models import Pump, Scheduler

""" create package instances"""
server = mws2.MicroWebSrv2()
pump = Pump(pin=23)
scheduler = Scheduler()

def create_application():
    """ main function and entry point to the package """

    """ register web routes """
    import bonsai_watering.controllers as controllers

    mws2.RegisterRoute(controllers.get_pump, mws2.GET, '/pump')
    mws2.RegisterRoute(controllers.post_pump, mws2.POST, '/pump')

    mws2.RegisterRoute(controllers.get_schedule, mws2.GET, '/schedule')
    mws2.RegisterRoute(controllers.post_schedule, mws2.POST, '/schedule')

    mws2.RegisterRoute(controllers.get_time, mws2.GET, '/time')
    mws2.RegisterRoute(controllers.post_time, mws2.POST, '/time')

    mws2.RegisterRoute(controllers.get_webrepl, mws2.GET, '/webrepl')

    """ schedule jobs """
    from bonsai_watering.jobs import water_plants

    scheduler.schedule(job=water_plants, at='07:00', pump=pump, duration=28)
    scheduler.schedule(job=water_plants, at='18:00', pump=pump, duration=17)

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
