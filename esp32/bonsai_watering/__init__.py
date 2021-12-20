import time
import MicroWebSrv2 as mws2
from bonsai_watering import models

''' create package instances'''
server = mws2.MicroWebSrv2()
scheduler = models.Scheduler()

def start_application():
    ''' main function and entry point to the package '''

    ''' register web routes '''
    from bonsai_watering import controllers, jobs, devices

    # /devices
    mws2.RegisterRoute(controllers.get_devices, mws2.GET, '/devices')
    mws2.RegisterRoute(controllers.post_devices, mws2.POST, '/devices/<name>')

    # /schedule
    mws2.RegisterRoute(controllers.get_schedule, mws2.GET, '/schedule')
    mws2.RegisterRoute(controllers.post_schedule, mws2.POST, '/schedule')
    mws2.RegisterRoute(controllers.update_schedule, mws2.PUT, '/schedule/<id>')
    mws2.RegisterRoute(controllers.delete_schedule, mws2.DELETE, '/schedule/<id>')

    # /time
    mws2.RegisterRoute(controllers.get_time, mws2.GET, '/time')
    mws2.RegisterRoute(controllers.post_time, mws2.POST, '/time')

    # /stats
    mws2.RegisterRoute(controllers.get_stats, mws2.GET, '/stats')

    ''' schedule jobs '''
    scheduler.schedule(job=jobs.water_plants, at='08:00', device=devices.pump, duration=6)

    ''' set up web server'''
    server.SetPacoConfig()
    server.StartManaged()

    ''' main program loop until keyboard interrupt '''
    try:
        while server.IsRunning:
            scheduler.run_scheduled()
            time.sleep(30)
    except KeyboardInterrupt:
        server.Stop()
        server.Log('Byee', server.DEBUG)
