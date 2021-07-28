import ujson
from bonsai_watering import logger

def get_logs(server, request):
    logs = logger.get_logs()
    json_logs = [ujson.dumps(log) for log in logs]

    request.Response.ReturnOkJSON(json_logs)
