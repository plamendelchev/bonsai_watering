from machine import RTC

class DateTime:
    def __init__(self, month, day, hour, minutes, seconds):
        self.month = month
        self.day = day
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
        self._rtc = RTC()

    @property
    def time(self):
        return (self.day, self.hour, self.minutes)

    @property
    def rtc(self):
        return self._rtc.datetime()

    @rtc.setter
    def rtc(self, value):
        self._rtc.datetime(value)

    @classmethod
    def now(cls):
        ''' returns a DateTime object '''

        now = list(RTC().datetime())
        for i in sorted((0, 3, 7), reverse=True): # delete unnecessary stuff
            del now[i]

        return cls(*now)

    @classmethod
    def parse(cls, at):
        '''
        `at` is in format '12:00'
        returns a DateTime object
        '''

        dt = cls.now()
        dt.hour, dt.minutes = [int(i) for i in at.split(':')]

        return dt

    def tomorrow(self):
        month, day = self.month, self.day

        if (day == 31 and month in (1, 3, 5, 7, 8, 10, 12) or
            day == 30 and month in (4, 6, 9, 11) or
            day in (28, 29) and month == 2):

            # update day
            day = 1

            # update month
            if month == 12: month = 1
            else: month += 1

        else:
            day += 1

        self.month, self.day = month, day

    def __repr__(self):
        return repr(['{:02d}/{:02d}'.format(self.day, self.month), '{:02d}:{:02d}'.format(self.hour, self.minutes)])
