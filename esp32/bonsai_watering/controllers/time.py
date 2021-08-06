import machine
from bonsai_watering import scheduler

rtc = machine.RTC()

def get_time(server, request):
    request.Response.ReturnOkJSON({'datetime': rtc.datetime()})

def post_time(server, request):
    data = request.GetPostedJSONObject()
    try:
        rtc.datetime(tuple(data))
    except ValueError:
        request.Response.ReturnJSON(400, {'error': 'Incorrect datetime format'})
        return
    request.Response.ReturnOkJSON({'datetime': rtc.datetime()})
