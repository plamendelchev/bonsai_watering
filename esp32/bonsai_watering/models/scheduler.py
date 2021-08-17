from . import DateTime

class Scheduler:
    def __init__(self):
        self.current_id = 0
        self._scheduled_jobs = []

    @property
    def scheduled_jobs(self):
        return [job.all_attributes for job in self._scheduled_jobs]

    def schedule(self,job , at, **kwargs):
        job = Job(self.current_id, job, at, **kwargs)

        self._scheduled_jobs.append(job)
        self.current_id += 1

        return job

    def unschedule(self, id):
        job = self._scheduled_jobs.pop(id)
        return(job.all_attributes)

    def run_scheduled(self):
        for job in self._scheduled_jobs:
            if job.at.time == DateTime.now().time:
                job.run()
                #server.Log(job, server.DEBUG)

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
    def __init__(self, id, job, at, **kwargs):
        self.id = id
        self.job = job
        self.args = kwargs
        self.at = at

    @property
    def at(self):
        return self._at

    @at.setter
    def at(self, value):
        # parse `value` ('12:00') into a datetime valid format
        dt_at = DateTime.parse(value)

        # check if job should be rescheduled for tomorrow
        if dt_at.time < DateTime.now().time:
            self._at = dt_at
            self._at.tomorrow()
        else:
            self._at = dt_at

    @property
    def all_attributes(self):
        return {
            'id': self.id,
            'job': self.job.__name__,
            'at': ['{:02d}/{:02d}'.format(self.at.day, self.at.month), '{:02d}:{:02d}'.format(self.at.hour, self.at.minutes)],
            #'args': {'pump': self.args['pump'].all_attributes, 'duration': self.args['duration']}  ## THIS IS NOT OK
            'pump': self.args['pump'].pin,
            'duration': self.args['duration']
        }

    def __call__(self):
        self.run()

    def run(self):
        # Execute job
        self.job(**self.args)

        # Update Day to tomorrow
        self.at.tomorrow()
