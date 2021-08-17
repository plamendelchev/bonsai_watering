from bonsai_watering import pump

def get_pump(server, request):
    ''' GET /pump '''
    request.Response.ReturnOkJSON(pump.all_attributes)

def post_pump(server, request):
    '''
    POST /pump
    expected json data -> {"status": [01]}
    '''

    data = request.GetPostedJSONObject()

    try:
        pump.status = int(data['status'])
    except KeyError:
        request.Response.ReturnJSON(400, {'error': 'Incorrect post data'})
    else:
        request.Response.ReturnOkJSON(pump.all_attributes)
