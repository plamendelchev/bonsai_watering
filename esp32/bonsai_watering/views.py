import gc

def to_json(item):
    gc.collect()
    return eval(repr(item))
