from app import mws2, pump

def get_pump(mws2, request):
    request.Response.ReturnOkJSON(pump.status)

def post_pump(msw2, request):
    data = request.GetPostedJSONObject()
    try:
        pump.status = int(data['status'])
    except KeyError:
        request.Response.ReturnBadRequest()
        return

    request.Response.ReturnOkJSON(pump.status)
