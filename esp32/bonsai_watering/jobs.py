import time

def get(job_name):
    return jobs[job_name]

def water_plants(device, duration):
    device.status = 1
    time.sleep(duration)
    device.status = 0

jobs = {'water_plants': water_plants}
