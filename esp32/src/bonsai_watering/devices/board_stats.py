import esp32, gc, os

from .base_device import BaseDevice

class BoardStats(BaseDevice):
    @property
    def status(self):
        temp = self.temp()
        memory_usage = self.memory()
        unix_ts = self.time()
        return self.to_json({'raw_temp': temp, 'mem_alloc': memory_usage[0], 'mem_free': memory_usage[1], 'mem_total': memory_usage[2], 'ts': unix_ts})

    def temp(self):
        temp = (esp32.raw_temperature() - 32) / 1.8
        return '{:.1f}'.format(temp)

    def memory(self):
        ''' return values in KB '''
        gc.collect()
        free, alloc = (gc.mem_free() / 1024), (gc.mem_alloc() / 1024)
        return (alloc, free, free + alloc)

    def storage(self):
        ''' returns values in MB '''
        storage = os.statvfs('/')
        available = float('{:.3f}'.format((storage[0] * storage[3]) / 1048576))
        total = float('{:.3f}'.format((storage[0] * storage[2]) / 1048576))
        return used, available, total - available
