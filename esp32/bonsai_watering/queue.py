from ucollections import namedtuple

Message = namedtuple('Message', ['data', 'topic'])
queue = []

def append(data, topic):
    message = Message(data, topic)
    queue.append(message)

def get_last_message():
    return queue.pop(0)
