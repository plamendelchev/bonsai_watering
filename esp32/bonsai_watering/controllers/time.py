import machine
from bonsai_watering import models

rtc = machine.RTC()

def get_time(server, request):
    request.Response.ReturnOkJSON(models.DateTime.now().rtc)

def post_time(server, request):
    try:
        data = request.GetPostedJSONObject()
        models.DateTime.rtc = tuple(data)
    except ValueError:
        request.Response.ReturnJSON(400, {'error': 'Incorrect datetime format'})
    else:
        request.Response.ReturnOkJSON(models.DateTime.now().rtc)
