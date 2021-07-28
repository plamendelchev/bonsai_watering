from bonsai_watering import pump, scheduler
from bonsai_watering.jobs import water_plants

def get_pump(server, request):
    request.Response.ReturnOkJSON({'status': pump.status})

def post_pump(server, request):
    ''' expected json data -> {"status": [01]} '''

    data = request.GetPostedJSONObject()

    try:
        pump.status = int(data['status'])
    except KeyError:
        request.Response.ReturnJSON(400, {'error': 'Incorrect post data'})
        return
    else:
        request.Response.ReturnOkJSON({'status': pump.status})

def get_pump_schedule(server, request):
    request.Response.ReturnOkJSON(scheduler.scheduled_jobs)

def post_pump_schedule(server, request):
    ''' expected json data -> {"job": "water_plants", "at": "12:00", "pump": "pump", "duration": 10} '''

    data = request.GetPostedJSONObject()

    try:
        job = scheduler.schedule(job=eval(data['job']), at=data['at'], pump=eval(data['pump']), duration=data['duration'])
    except (KeyError, TypeError):
        request.Response.ReturnJSON(400, {'error': 'Incorrect post data'})
        return
    except NameError as err:
        request.Response.ReturnJSON(400, {'error': str(err)})
        return
    else:
        request.Response.ReturnOkJSON(job)

