import ujson

def to_json(item):
    return ujson.dumps(eval(repr(item)))
