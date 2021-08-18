from bonsai_watering import devices

def get_pump(server, request):
    ''' GET /pump '''
    request.Response.ReturnOkJSON(devices.pump.all_attributes)

def post_pump(server, request):
    '''
    POST /pump
    expected json data -> {"status": [01]}
    '''

    data = request.GetPostedJSONObject()

    try:
        devices.pump.status = int(data['status'])
    except KeyError:
        request.Response.ReturnJSON(400, {'error': 'Incorrect post data'})
    else:
        request.Response.ReturnOkJSON(devices.pump.all_attributes)
