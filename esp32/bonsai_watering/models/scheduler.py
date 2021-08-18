from .datetime import DateTime
from bonsai_watering import jobs, devices

class Scheduler:
    def __init__(self):
        self.current_id = 1
        self._scheduled_jobs = []

    @property
    def scheduled_jobs(self):
        return [job.all_attributes for job in self._scheduled_jobs]

    def schedule(self, job, at, device, **kwargs):
        # retrieve func from job list
        job_func = jobs.get(job) # raises KeyError if job is not found

        # retrieve device from device list 
        device_inst = devices.get(device) # raises KeyError if device is not found

        job = Job(self.current_id, job_func, at, device_inst, **kwargs)

        self._scheduled_jobs.append(job)
        self.current_id += 1

        return job

    def unschedule(self, id):
        job = self._scheduled_jobs.pop(id)
        return(job.all_attributes)

    def run_scheduled(self):
        for job in self._scheduled_jobs:
            job.run()
#            if job.at.time == DateTime.now().time:
#                job.run()

    def get_job(self, id):
        return self._scheduled_jobs[id]

    def update_job(self, id, data):
        job = self.get_job(id=id)

        for attr, value in data.items():
            if not hasattr(job, attr):
                raise AttributeError(attr)
            setattr(job, attr, value)

        self._scheduled_jobs[id] = job
        return job


class Job:
    def __init__(self, id, job, at, device, is_active=True, duration=0, **kwargs):
        self.id = id
        self.job = job
        self.at = at
        self.device = device
        self.is_active = is_active
        self.duration = duration
        self.args = kwargs

    @property
    def at(self):
        return self._at

    @at.setter
    def at(self, value):
        # parse `value` ('12:00') into a datetime valid format
        self._at = DateTime.parse(value)

        # check if job should be rescheduled for tomorrow
        if self._at.time < DateTime.now().time:
            self._at.tomorrow()

    @property
    def all_attributes(self):
        return {
            'id': self.id,
            'job': self.job.__name__,
            'is_active': self.is_active,
            'at': ['{:02d}/{:02d}'.format(self.at.day, self.at.month), '{:02d}:{:02d}'.format(self.at.hour, self.at.minutes)],
            'device': {'pin': self.device.pin, 'type': self.device.__class__.__name__},
            'duration': self.duration
        }

    def __call__(self):
        self.run()

    def run(self):
        if not self.is_active or not self.at.time == DateTime.now().time:
            return

        # Execute job
        #self.job(**self.args)
        self.job(self.device, self.duration, **self.args)

        # Update Day to tomorrow
        self.at.tomorrow()
