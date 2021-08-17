import esp
import network
import machine
import ntptime

esp.osdebug(None)

def do_connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass

    print('network config:', wlan.ifconfig())

def set_ntp_time(timezone=0):
    try:
        ntptime.settime()

        rtc = machine.RTC()
        current_time = list(rtc.datetime())
        current_time[4] += timezone

        rtc.datetime(current_time)
    except OSError:
        print('Unable to set time. ')

home = {'ssid': '', 'password': ''}

do_connect(**home)
set_ntp_time(timezone=3)
