import utime

class Scheduler:
    def __init__(self):
        self.scheduled_jobs = []

    def schedule(self, function, at):
        job = Job(function, at)

        self.scheduled_jobs.append(job)

    def run_scheduled(self):
        now = utime.localtime()[1:-3]

        for job in self.scheduled_jobs:
            if job.at == now:
                job()

class Job:
    def __init__(self, job, at):
        self.job = job
        self.at = at

    @property
    def at(self):
        return tuple(self._at)

    @at.setter
    def at(self, value):
        self._at = self._validate_time(value)

    def _validate_time(self, at):
        hour = at.split(':')

        # list only with month, day, hour and minute
        time = list(utime.localtime()[1:-3])
        # set hour:minute to the provided one
        time[2:] = [int(i) for i in hour]

        return time

    def _tomorrow(self):
        # (4, 22, 11, 30)
        month, day = self._at[:2]

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

        self._at[:2] = month, day

    def __call__(self):
        # Execute job
        self.job()
        # Update Day to tomorrow
        self._tomorrow()
