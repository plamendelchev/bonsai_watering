import time

import MicroWebSrv2 as mws2

from bonsai_watering.models import Pump, Scheduler

pump = Pump(pin=23)

def create_application():
    """ create pump """

    """ create and configure an instance of a MicroWebSrv2 """
    server = mws2.MicroWebSrv2()
    server.SetEmbeddedConfig()

    """ register web routes """
    from bonsai_watering.controllers import get_pump, post_pump

    mws2.RegisterRoute(get_pump, mws2.GET, '/pump')
    mws2.RegisterRoute(post_pump, mws2.POST, '/pump')

    """ schedule jobs """
    scheduler = Scheduler()

    from bonsai_watering.jobs import water_plants
    scheduler.schedule(job=water_plants, at='00:57', pump=pump, duration=10)

    """ start web server instance """
    server.StartManaged()

    """ main program loop until keyboard interrupt """
    try:
        while server.IsRunning:
            scheduler.run_scheduled()
            time.sleep(2)
    except KeyboardInterrupt:
        server.Stop()
        print('Bye')
