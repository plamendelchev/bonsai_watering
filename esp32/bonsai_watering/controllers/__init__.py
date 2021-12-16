import ujson

def parse(message):
    raw_data = message.decode('utf-8')
    data = ujson.loads(raw_data)

    return raw_data, data

def get_argument(topic):
    return topic.decode('utf-8').split('/')[-1]

from .devices import *
from .time import *
from .schedule import *
from .update import *
from .stats import *
