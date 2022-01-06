import ntptime
from machine import RTC

def set_ntp_time(tz=0):
    try:
        print('Setting up NTP Time ...')
        ntptime.settime()

        rtc = RTC()
        current_time = list(rtc.datetime())
        current_time[4] += tz

        rtc.datetime(current_time)
        print('NTP Time OK: {}'.format(rtc.datetime()))
    except OSError:
        print('Unable to set up NTP time. ')
