#from ucollections import namedtuple
#
#Message = namedtuple('Message', ['data', 'topic'])
from bonsai_watering import models

queue = []

def append(data, topic):
    message = models.Message(data, topic)
    queue.append(message)

def get_last_message():
    return queue.pop(0)
