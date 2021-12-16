from bonsai_watering import scheduler, jobs, devices, views, controllers, queue

def get_schedule(server, request):
    ''' GET /schedule '''
    request.Response.ReturnOkJSON(views.to_json(scheduler.scheduled_jobs))

def set_schedule(topic, message, response_topic=None):
    '''
    bonsai_watering/set/schedule/<id>
    expected json data -> {"job": "water_plants", "at": "12:00", "device": "pump", "duration": 10}
    '''

    schedule_id = controllers.get_argument(topic)
    try:
        raw_data, data = controllers.parse(message)
        job_func = jobs.get(data['job'])
        device = devices.get(data['device'])
        data['job'], data['service'] = job_func, device
        job = scheduler.schedule(**data)
    except (KeyError, TypeError, SyntaxError, NameError):
        data = {'error': 'Incorrect data `{}`'.format(raw_data)}
        queue.append(data=views.to_json(data), topic='bonsai_watering/errors')

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
