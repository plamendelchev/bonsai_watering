import time

import MicroWebSrv2 as mws2

from bonsai_watering.models import Pump, Scheduler


def create_application():
    """ create instances of objects """
    pump = Pump(pin=23)
    scheduler = Scheduler()

    """ create and configure an instance of a MicroWebSrv2 """
    server = mws2.MicroWebSrv2()
    server.SetEmbeddedConfig()

    """ register web routes """
    from bonsai_watering.controllers import get_pump, post_pump

    server.RegisterRoute(get_pump, mws2.GET, '/pump')
    server.RegisterRoute(post_pump, mws2.POST, '/pump')

    """ schedule jobs """
#    from bonsai_watering.jobs import water_plants
#
#    scheduler.schedule(water_plants, at='10:00')

    """ start web server instance """
    server.StartManaged()

    """ main program loop until keyboard interrupt """
    try:
        while server.IsRunning:
            time.sleep(1)
            scheduler.run_scheduled()
    except KeyboardInterrupt:
        server.Stop()
        print('Bye')
