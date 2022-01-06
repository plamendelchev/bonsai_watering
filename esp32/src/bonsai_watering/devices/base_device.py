import ujson, utime

class BaseDevice:
    def __init__(self, topic):
        self.topic = topic
    def time(self):
        return str(946684800 + utime.time())
    def to_json(self, value):
        return ujson.dumps(value)
