from datetime import DateTime

def get_time(server, request):
    request.Response.ReturnOkJSON(DateTime.now().rtc)

def post_time(server, request):
    try:
        data = request.GetPostedJSONObject()
        DateTime.rtc = tuple(data)
    except ValueError:
        request.Response.ReturnJSON(400, {'error': 'Incorrect datetime format'})
    else:
        request.Response.ReturnOkJSON(DateTime.now().rtc)
