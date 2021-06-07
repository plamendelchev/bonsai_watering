import utime

class Scheduler:
    def __init__(self):
        self.scheduled_jobs = []

    def schedule(self,job , at, **kwargs):
        job = Job(job, at, **kwargs)

        self.scheduled_jobs.append(job)

    def run_scheduled(self):
        now = DateTime.now()

        for job in self.scheduled_jobs:
            if job.at == now:
                job.run()
                server.Log(job, server.DEBUG)


class Job:
    def __init__(self, job, at, **kwargs):
        self.job = job
        self.at = DateTime(at)
        self.args = kwargs

    def __repr__(self):
        return '{}(job={}, at={}, args={})'.format(self.__class__.__name__, self.job, self.at, self.args)

    def __call__(self):
        self.run()

    def run(self):
        # Execute job
        self.job(**self.args)

        # Update Day to tomorrow
        self.at = DateTime.tomorrow(self.at)


class DateTime:
    def __new__(cls, hour=str):
        '''hour is in the format "12:00"'''

        hour_minute = hour.split(':')
        time = DateTime.now()
        time[2:] = [int(i) for i in hour_minute]

        return time

    @staticmethod
    def now():
        return list(utime.localtime()[1:-3])

    @staticmethod
    def tomorrow(date_time):
        # (4, 22, 11, 30)
        month, day = date_time[:2]

        if (day == 31 and month in (1, 3, 5, 7, 8, 10, 12) or
            day == 30 and month in (4, 6, 9, 11) or
            day in (28, 29) and month == 2):

            # update day
            day = 1

            # update month
            if month == 12:
                month = 1
            else:
                month += 1

        else:
            day += 1

        date_time[:2] = month, day

        return date_time
