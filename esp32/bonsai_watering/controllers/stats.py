import gc
import os

from bonsai_watering import models, views

def get_ram():
    ''' return values in KB '''
    gc.collect()

    free, alloc = gc.mem_free(), gc.mem_alloc()
    total = free + alloc
    perc = '{0:.2f}'.format(free / total * 100)

    return models.Message(views.to_json({'free': free, 'total': total, 'perc': perc}), 'bonsai_watering/stats/ram')

def get_storage():
    ''' returns values in MB '''
    storage = os.statvfs('/')
    return models.Message(views.to_json({'available': '{:.3f}'.format((storage[0] * storage[3]) / 1048576)}), 'bonsai_watering/stats/storage')
