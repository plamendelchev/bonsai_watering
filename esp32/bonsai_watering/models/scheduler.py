from datetime import DateTime
from bonsai_watering import jobs, devices

class Scheduler:
    def __init__(self):
        self.current_id = 0
        self.scheduled_jobs = []

    def schedule(self, job, at, device, **kwargs):
        job = Job(self.current_id, job, at, device, **kwargs)

        self.scheduled_jobs.append(job)
        self.current_id += 1

        return job

    def unschedule(self, id):
        job = next(job for job in self.scheduled_jobs if job.id == id)
        self.scheduled_jobs.remove(job)
        return job

    def run_scheduled(self):
        for job in self.scheduled_jobs:
            job.run()

    def get_job(self, id):
        return self.scheduled_jobs[id]

    def update_job(self, id, data):
        job = self.get_job(id=id)

        for attr, value in data.items():
            if not hasattr(job, attr):
                raise AttributeError(attr)
            setattr(job, attr, value)

        self.scheduled_jobs[id] = job
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

    def run(self):
        self.__call__()

    def __repr__(self):
        return repr({
            'id': self.id,
            'job': self.job.__name__,
            'is_active': self.is_active,
            'at': self.at,
            'device': self.device,
            'duration': self.duration
        })

    def __call__(self):
        if not self.is_active:
            return
        if not self.at.time == DateTime.now().time:
            return

        # Execute job
        #self.job(**self.args)
        self.job(self.device, self.duration, **self.args)

        # Update Day to tomorrow
        self.at.tomorrow()
