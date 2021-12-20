import gc, os, machine, ujson

class BaseBoard:
    def __init__(self, topic):
        self.topic = topic
    def __repr__(self):
        return repr({'type': self.__class__.__name__, 'status': self.status, 'topic': self.topic})
    @property
    def status(self):
        pass
    def to_json(self, value):
        return ujson.dumps(value)

class BoardMemory(BaseBoard):
    @property
    def status(self):
        ''' return values in KB '''
        gc.collect()

        free, alloc = (gc.mem_free() / 1024), (gc.mem_alloc() / 1024)
        total = free + alloc
        perc = float('{0:.2f}'.format(free / total * 100))

        return self.to_json({'alloc': alloc, 'free': free, 'total': total, 'perc': perc})

class BoardStorage(BaseBoard):
    @property
    def status(self):
        ''' returns values in MB '''

        storage = os.statvfs('/')
        available = float('{:.3f}'.format((storage[0] * storage[3]) / 1048576))
        total = float('{:.3f}'.format((storage[0] * storage[2]) / 1048576))
        used = total - available

        return self.to_json({'used': used, 'available': available, 'total': total})

class BoardTime(BaseBoard):
    def __init__(self, topic):
        super().__init__(topic)
        self.rtc = machine.RTC()

    @property
    def status(self):
        return self.to_json(self.rtc.datetime())
