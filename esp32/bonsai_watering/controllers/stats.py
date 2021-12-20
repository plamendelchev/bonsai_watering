import gc
import os

from bonsai_watering import views

def get_ram():
    ''' return values in KB '''
    gc.collect()

    free, alloc = (gc.mem_free() / 1024), (gc.mem_alloc() / 1024)
    total = free + alloc
    perc = float('{0:.2f}'.format(free / total * 100))

    return {'alloc': alloc, 'free': free, 'total': total, 'perc': perc}

def get_storage():
    ''' returns values in MB '''
    storage = os.statvfs('/')
    available = float('{:.3f}'.format((storage[0] * storage[3]) / 1048576))
    total = float('{:.3f}'.format((storage[0] * storage[2]) / 1048576))

    return {'available': available, 'total': total}

def get_stats(server, request):
    ram, storage = get_ram(), get_storage()
    response = {'ram_kb': ram, 'storage_mb': storage}

    return request.Response.ReturnOkJSON(views.to_json(response))
