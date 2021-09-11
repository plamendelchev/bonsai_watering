from ucollections import namedtuple, dequeue

Message = namedtuple('Message', ['data', 'topic'])
queue = dequeue()

def append(data, topic):
    message = Message(data, topic)
    queue.append(message)

def get_last_message():
    return queue.popleft()
