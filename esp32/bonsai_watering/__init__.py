import uasyncio as asyncio
import mqtt_as

from bonsai_watering import devices

'''
mqtt topics
--

* Status report (publishing)
bonsai_watering/status/pump -> 0/1

bonsai_watering/status/board/temp -> 20
bonsai_watering/status/board/memory -> {"free": X, "alloc": X, "total": X}
bonsai_watering/status/board/storage -> {"free": X, "used": X, "total": X}
bonsai_watering/status/board/time -> linux timestamp

* Change requests (sub, we should pub immediately the changes)
bonsai_watering/set/pump -> 0/1

'''

def start_application():
    async def subscribe_to_topics(client):
        await client.subscribe(b'bonsai_watering/set/pump', 1)

    def callback(topic, message, retained):
        print('Received', (topic, message, retained))
        devices.change_status(topic, message)

    async def publish_status(client, devices, interval=15):
        while True:
            for device in devices:
                await client.publish(device.topic, str(device.status), qos=1)

            await asyncio.sleep(interval)

    async def main(client, devices, board_devices):
        await client.connect()

        await asyncio.gather(
            publish_status(client, devices, interval=30),
            publish_status(client, board_devices, interval=60)
        )

    ''' mqtt config '''
    mqtt_as.config['connect_coro'] = subscribe_to_topics # Defines a task to be run when a connection to the broker has been established
    mqtt_as.config['subs_cb'] = callback # Runs when a message is received whose topic matches a subscription

    ''' create mqtt instance '''
    mqtt_client = mqtt_as.MQTTClient(mqtt_as.config)
    mqtt_client.DEBUG = True

    ''' register devices '''
    devices.register_device(type=devices.PUMP, topic='bonsai_watering/status/pump', pin=23)

    ''' register board devices '''
    devices.register_device(type=devices.B_TEMP, topic='bonsai_watering/status/board/temp')
    devices.register_device(type=devices.B_MEMORY, topic='bonsai_watering/status/board/memory')
    devices.register_device(type=devices.B_STORAGE, topic='bonsai_watering/status/board/storage')
    devices.register_device(type=devices.B_TIME, topic='bonsai_watering/status/board/time')

    ''' main program loop '''
    asyncio.run(main(mqtt_client, devices=devices.devices, board_devices=devices.board_devices))
