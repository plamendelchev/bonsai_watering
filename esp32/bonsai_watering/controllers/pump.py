from bonsai_watering import pump

def get_pump(server, request):
    request.Response.ReturnOkJSON({'status': pump.status})

def post_pump(server, request):
    data = request.GetPostedJSONObject()
    try:
        pump.status = int(data['status'])
    except KeyError:
        request.ResponseReturnJSON(400, {'error': 'Incorrect post data'})
        return

    request.Response.ReturnOkJSON({'status': pump.status})
