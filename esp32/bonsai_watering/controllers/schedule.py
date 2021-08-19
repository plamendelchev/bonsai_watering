from bonsai_watering import scheduler, jobs, devices, views

def get_schedule(server, request):
    ''' GET /schedule '''
    request.Response.ReturnOkJSON(views.to_json(scheduler.scheduled_jobs))

def post_schedule(server, request):
    '''
    POST /schedule
    expected json data -> {"job": "water_plants", "at": "12:00", "device": "pump", "duration": 10}
    '''

    data = request.GetPostedJSONObject()

    try:
        # Find job from list
        job_func = jobs.get(data['job'])
#        data['job'] = job_func
        # Find device from list 
        device_inst = devices.get(data['device'])

        data['job'], data['device'] = job_func, device_inst

        job = scheduler.schedule(**data)
    except (KeyError, TypeError, SyntaxError):
        request.Response.ReturnJSON(400, {'error': 'Incorrect post data'})
    except NameError as err:
        request.Response.ReturnJSON(400, {'error': str(err)})
    else:
        request.Response.ReturnOkJSON(views.to_json(job))

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
        request.Response.ReturnOkJSON(views.to_json(job))


def delete_schedule(server, request, args):
    ''' DELETE /schedule/<id> '''

    try:
        job = scheduler.unschedule(args['id'])
    except (IndexError, TypeError):
        request.Response.ReturnJSON(400, {'error': 'Invalid id'})
    else:
        request.Response.ReturnOkJSON(views.to_json(job))
