from bonsai_watering import scheduler

def get_schedule(server, request):
    ''' GET /schedule '''
    request.Response.ReturnOkJSON(scheduler.scheduled_jobs)

def post_schedule(server, request):
    '''
    POST /schedule
    expected json data -> {"job": "water_plants", "at": "12:00", "device": "pump", "duration": 10}
    '''

    data = request.GetPostedJSONObject()

    try:
        job = scheduler.schedule(**data)
    except (KeyError, TypeError, SyntaxError):
        request.Response.ReturnJSON(400, {'error': 'Incorrect post data'})
    except NameError as err:
        request.Response.ReturnJSON(400, {'error': str(err)})
    else:
        request.Response.ReturnOkJSON(job.all_attributes)

def update_schedule(server, request, args):
    ''' PUT /schedule/<id> '''

    data = request.GetPostedJSONObject()

    try:
        job = scheduler.update_job(id=args['id'], data=data)
    except IndexError:
        request.Response.ReturnJSON(400, {'error': 'Invalid id'})
    except AttributeError as err:
        request.Response.ReturnJSON(400, {'error': 'Incorrect key \'{}\''.format(err)})
    except ValueError:
        request.Response.ReturnJSON(400, {'error': 'Incorrect value'})
    else:
        request.Response.ReturnOkJSON(job.all_attributes)


def delete_schedule(server, request, args):
    ''' DELETE /schedule/<id> '''

    try:
        job = scheduler.unschedule(args['id'])
    except (IndexError, TypeError):
        request.Response.ReturnJSON(400, {'error': 'Invalid id'})
    else:
        request.Response.ReturnOkJSON(job)
