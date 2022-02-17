import uasyncio as asyncio
import mqtt_as

from bonsai_watering import devices, time

'''
mqtt topics
--

* Status report (publishing)
bonsai/status/common -> {"temp": 20, "humidity": 50, "sunlight": 40, "reservoir_alert": 0, "ts": "1640786943"}
bonsai/status/plants/elk -> {"pump": 0, "sprayer": 0, "moisture": 20, "ts": "1640786943"}
bonsai/status/board -> {"raw_temp": 40, "mem_alloc": 100, "mem_free": 200, "mem_total": 300, "ts":"1640786943"}

* Change requests (sub)
bonsai_watering/set/plants/elk -> {"pump": 1}

'''


def start_application():
    def callback(topic, message, retained):
        print('Received', (topic, message, retained))
        devices.change_status(topic, message)

    async def subscribe_to_topics(client):
        await client.subscribe(b'bonsai/set/plants/+', 1)

    async def publish_status(client, devices, interval=15):
        while True:
            async for device in devices:
                await client.publish(device.topic, device.status, qos=1)

            await asyncio.sleep(interval)

    async def main(client):
        await client.connect()

        time.set_ntp_time(tz=+2)

        await asyncio.gather(
            publish_status(client, devices.devices, interval=30),
            publish_status(client, devices.board_devices, interval=60)
        )

    ''' mqtt config '''
    mqtt_as.config['connect_coro'] = subscribe_to_topics # Defines a task to be run when a connection to the broker has been established
    mqtt_as.config['subs_cb'] = callback # Runs when a message is received whose topic matches a subscription

    ''' create mqtt instance '''
    mqtt_client = mqtt_as.MQTTClient(mqtt_as.config)
    mqtt_client.DEBUG = True

    ''' register devices '''
    devices.register_device(type=devices.PLANT, topic='bonsai/status/plants/default', pins={'pump': 23, 'sprayer': 24, 'moisture': 25})
    devices.register_device(type=devices.COMMON, topic='bonsai/status/common', pins={'dht22': 20 , 'sunlight': 21, 'reservoir': 22})
    devices.register_device(type=devices.BOARD_STATS, topic='bonsai/status/board')

    ''' main program loop '''
    try:
        asyncio.run(main(mqtt_client))
    except (KeyboardInterrupt, SystemExit):
        pass
