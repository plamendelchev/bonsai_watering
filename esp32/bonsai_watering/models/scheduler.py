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

    def run_scheduled(self):
        for job in self._scheduled_jobs:
            if job.at.time == DateTime.now().time:
                job.run()
                #server.Log(job, server.DEBUG)


class Job:
    def __init__(self, id, job, at, **kwargs):
        self.id = id
        self.job = job
        self.args = kwargs

        # parse `at` ('12:00') into a datetime valid value
        dt_at = DateTime.parse(at)

        # check if job should be rescheduled for tomorrow
        if dt_at.time < DateTime.now().time:
            self.at = dt_at
            self.at.tomorrow()
        else:
            self.at = dt_at

    @property
    def all_attributes(self):
        return {
            'id': self.id,
            'job': self.job.__name__,
            'at': ['{:02d}/{:02d}'.format(self.at.day, self.at.month), '{:02d}:{:02d}'.format(self.at.hour, self.at.minutes)],
            'args': {'pump': self.args['pump'].all_attributes, 'duration': self.args['duration']}  ## THIS IS NOT OK
        }

    def __call__(self):
        self.run()

    def run(self):
        # Execute job
        self.job(**self.args)

        # Update Day to tomorrow
        self.at.tomorrow()
