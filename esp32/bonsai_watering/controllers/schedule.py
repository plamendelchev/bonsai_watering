from bonsai_watering import pump, scheduler
from bonsai_watering.jobs import water_plants

def get_schedule(server, request):
    ''' GET /schedule '''
    request.Response.ReturnOkJSON(scheduler.scheduled_jobs)

def post_schedule(server, request):
    '''
    POST /schedule
    expected json data -> {"job": "water_plants", "at": "12:00", "pump": "pump", "duration": 10} '''

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
