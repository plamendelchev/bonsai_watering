import gc
import ujson

def to_json(item):
    gc.collect()
    return ujson.dumps(eval(repr(item)))
