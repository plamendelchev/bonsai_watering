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

def set_ntp_time():
    try:
        ntptime.settime()

        rtc = machine.RTC()
        current_time = list(rtc.datetime())
        current_time[4] += 3

        rtc.datetime(current_time)
    except OSError:
        print('Unable to set time. ')


wifi_cred = {'ssid': '', 'password': ''}

do_connect(**wifi_cred)
set_ntp_time()
