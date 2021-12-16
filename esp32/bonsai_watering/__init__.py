import time
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
DONE `bonsai_watering/set/devices/<device_name>` '{"status": 1}'
bonsai_watering/set/schedule/<id> '{"is_active": 0}'

* Create requests
bonsai_watering/new/schedule/ '{"job": "water_plants"}'

* Delete requests
bonsai_watering/delete/schedule/<id>
'''
from bonsai_watering import models
scheduler = models.Scheduler()

from bonsai_watering import queue, controllers, routes

def callback(topic, msg, retained):
    print('Received', (topic, msg, retained))
    routes.run_controller(topic, msg)

async def conn_han(client):
    # /devices
    routes.register_route(controller=controllers.set_devices,
                               topic=b'bonsai_watering/set/devices/pump')

#    # /schedule
    routes.register_route(controller=controllers.set_schedule,
                              topic=b'bonsai_watering/set/schedule/+')

    for topic in routes.topics():
        await client.subscribe(topic, 1)

async def publish_queue_messages(client, interval=5):
    while True:
        try:
            message = queue.get_last_message()
        except IndexError:
            pass
        else:
            await client.publish(message.topic, message.data, qos=1)

        await asyncio.sleep(interval)

async def publish_board_stats(client, interval=60):
    while True:
        ram = controllers.get_ram()
        storage = controllers.get_storage()

        await client.publish(ram.topic, ram.data, qos=1)
        await client.publish(storage.topic, storage.data, qos=1)

        await asyncio.sleep(interval)

async def publish_device_status(client, interval=10):
    while True:
        for device in controllers.get_devices():
            await client.publish(device.topic, device.data, qos=1)

        await asyncio.sleep(interval)

async def publish_schedule_status(client, interval=10):
    while True:
        pass

async def main(client):
    await client.connect()

    await asyncio.gather(
        publish_device_status(client, interval=10),
        publish_schedule_status(client, interval=10),
        publish_queue_messages(client, interval=30),
        publish_board_stats(client, interval=60)
    )


from bonsai_watering import config

''' mqtt config '''
config.config['subs_cb'] = callback # Runs when a message is received whose topic matches a subscription
config.config['connect_coro'] = conn_han # Defines a task to run when a connection to the broker has been established

''' create package instances'''
mqtt_client = mqtt_as.MQTTClient(config.config)
mqtt_client.DEBUG = True

def start_application():
    ''' main function and entry point to the package '''

    ''' register devices '''
    from bonsai_watering import devices

    devices.register_device(name='pump', type='Pump', pin=23, pub_topic=b'bonsai_watering/status/devices/pump')

    ''' register web routes '''
    #from bonsai_watering import controllers, jobs, devices

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
#    try:
#        asyncio.run(main(mqtt_client))
#    except Exception as ex:
#        print(ex)
#        mqtt_client.close()  # Prevent LmacRxBlk:1 errors
    asyncio.run(main(mqtt_client))
