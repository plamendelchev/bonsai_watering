from bonsai_watering import devices, views

def get_devices(server, request):
    ''' GET /devices '''
    request.Response.ReturnOkJSON(views.to_json(devices.devices))

def post_devices(server, request, args):
    '''
    POST /devices/<name>
    expected json data -> {"status": [01]}
    '''

    try:
        data = request.GetPostedJSONObject()
        device = devices.get(args['name'])
        device.status = int(data['status'])
    except (TypeError, KeyError):
        request.Response.ReturnJSON(400, {'error': 'Incorrect post data'})
    except StopIteration:
        request.Response.ReturnJSON(400, {'error': 'Incorrect device name'})
    else:
        request.Response.ReturnOkJSON(views.to_json(device))
