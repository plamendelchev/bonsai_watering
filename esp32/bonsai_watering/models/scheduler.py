#from bonsai_watering import logger
from . import Logger, DateTime

logger = Logger()

class Scheduler:
    def __init__(self):
        self._scheduled_jobs = []

    @property
    def scheduled_jobs(self):
        return [job.all_attributes for job in self._scheduled_jobs]

    def schedule(self,job , at, **kwargs):
        job = Job(job, at, **kwargs)
        self._scheduled_jobs.append(job)

        return job

    def run_scheduled(self):
        for job in self._scheduled_jobs:
            if job.at.time == DateTime.now().time:
                job.run()
                #server.Log(job, server.DEBUG)
                #logger.append(date=now, job=job.__repr__())


class Job:
    def __init__(self, job, at, **kwargs):
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
            'job': self.job.__name__,
            'at': ['{}/{}'.format(self.at.day, self.at.month), '{}:{}'.format(self.at.hour, self.at.minutes)],
            'args': {'pump': self.args['pump'].all_attributes, 'duration': self.args['duration']}  ## THIS IS NOT OK
        }

    def __call__(self):
        self.run()

    def run(self):
        # Execute job
        self.job(**self.args)

        # Update Day to tomorrow
        self.at.tomorrow()
