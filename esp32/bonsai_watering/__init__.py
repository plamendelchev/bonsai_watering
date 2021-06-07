import time

import MicroWebSrv2 as mws2

from bonsai_watering.models import Pump, Scheduler

""" create pump """
pump = Pump(pin=23)

def create_application():

    """ create and configure an instance of a MicroWebSrv2 """
    server = mws2.MicroWebSrv2()
    server.SetEmbeddedConfig()

    """ register web routes """
    from bonsai_watering.controllers import get_pump, post_pump

    mws2.RegisterRoute(get_pump, mws2.GET, '/pump')
    mws2.RegisterRoute(post_pump, mws2.POST, '/pump')

    """ schedule jobs """
    from bonsai_watering.jobs import water_plants

    scheduler = Scheduler()
    scheduler.schedule(job=water_plants, at='20:15', pump=pump, duration=10)
    scheduler.schedule(job=water_plants, at='20:16', pump=pump, duration=5)

    """ start web server instance """
    server.StartManaged()

    """ main program loop until keyboard interrupt """
    try:
        while server.IsRunning:
            scheduler.run_scheduled()
            time.sleep(2)
    except KeyboardInterrupt:
        server.Stop()
        server.Log('Byee', server.DEBUG)
