import MicroWebSrv2 as mws2

from bonsai_watering.models import Pump, Scheduler, Job

pump = Pump(pin=23)
server = mws2.MicroWebSrv2()
scheduler = Scheduler()
