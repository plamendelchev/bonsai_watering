import time

print('Sleeping a bit')
time.sleep(1)
print('Done Sleeping')


import mqtt_as
import uasyncio as asyncio

'''
mqtt topics
--

* Broker status
bonsai_watering/connected

* Status report (publishing)
bonsai_watering/status/devices

* Active get
bonsai_watering/get/{devices,schedule,time}

* Change requests
`bonsai_watering/set/devices/<device_name>` '{"status": 1}' -> It publishes a response to `bonsai_watering/status/devices/<device_name>`
bonsai_watering/set/schedule/<id> '{"is_active": 0}'

* Create requests
bonsai_watering/new/schedule/ '{"job": "water_plants"}'

* Delete requests
bonsai_watering/delete/schedule/<id>
'''


def callback(topic, msg, retained):
    print('Received', (topic, msg, retained))
    controllers.call(topic, msg)

async def conn_han(client):
#    await client.subscribe('bonsai_watering/set/#', 1)
#    await client.subscribe('bonsai_watering/new/#', 1)
#    await client.subscribe('bonsai_watering/delete/#', 1)
    topics = [route.topic for route in controllers.routes]
    for topic in topics:
        await client.subscribe(topic, 1)

from bonsai_watering import queue

async def main(client):
    await client.connect()

    while True:
        try:
            message = queue.get_last_message()
        except IndexError:
            pass
        else:
            await client.publish(message.topic, message.data, qos=1)

        await asyncio.sleep(5)

from bonsai_watering import config, models

''' mqtt config '''
config.config['subs_cb'] = callback # Runs when a message is received whose topic matches a subscription
config.config['connect_coro'] = conn_han # Defines a task to run when a connection to the broker has been established

''' create package instances'''
scheduler = models.Scheduler()
mqtt_client = mqtt_as.MQTTClient(config.config)
mqtt_client.DEBUG = True

def start_application():
    ''' main function and entry point to the package '''

    ''' register web routes '''
    #from bonsai_watering import controllers, jobs, devices
    from bonsai_watering import controllers

    # /devices
    controllers.register_route(controllers.set_devices,
                               topic=b'bonsai_watering/set/devices/pump',
                               response_topic=b'bonsai_watering/status/devices/pump')

    controllers.register_route(controllers.set_devices,
                               topic=b'bonsai_watering/set/devices/pump2',
                               response_topic=b'bonsai_watering/status/devices/pump2')
#    mws2.RegisterRoute(controllers.get_devices, mws2.GET, '/devices')
#    mws2.RegisterRoute(controllers.post_devices, mws2.POST, '/devices/<name>')

#    # /schedule
#    mws2.RegisterRoute(controllers.get_schedule, mws2.GET, '/schedule')
#    mws2.RegisterRoute(controllers.post_schedule, mws2.POST, '/schedule')
#    mws2.RegisterRoute(controllers.update_schedule, mws2.PUT, '/schedule/<id>')
#    mws2.RegisterRoute(controllers.delete_schedule, mws2.DELETE, '/schedule/<id>')
#
#    # /time
#    mws2.RegisterRoute(controllers.get_time, mws2.GET, '/time')
#    mws2.RegisterRoute(controllers.post_time, mws2.POST, '/time')
#
#    # /webrepl
#    mws2.RegisterRoute(controllers.get_webrepl, mws2.GET, '/webrepl')

    ''' schedule jobs '''
#    scheduler.schedule(job=jobs.water_plants, at='07:00', device=devices.pump, duration=20)
#    scheduler.schedule(job=jobs.water_plants, at='18:00', device=devices.pump, duration=10)


    ''' main program loop '''
    try:
        asyncio.run(main(mqtt_client))
    except Exception as ex:
        print(ex)
        mqtt_client.close()  # Prevent LmacRxBlk:1 errors
