
def get_webrepl(server, request):
    request.Response.ReturnOkJSON({'success': 'Shutting down server'})
    server.Stop()
