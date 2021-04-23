from app.common import server, pump, mws2

@mws2.WebRoute(mws2.GET, '/pump')
def get_pump(server, request):
    request.Response.ReturnOkJSON(pump.status)

@mws2.WebRoute(mws2.POST, '/pump')
def post_pump(server, request):
    data = request.GetPostedJSONObject()
    try:
        pump.status = int(data['status'])
    except KeyError:
        request.ResponseReturnJSON(400, {'error': 'Incorrect post data'})
        return

    request.Response.ReturnOkJSON(pump.status)
