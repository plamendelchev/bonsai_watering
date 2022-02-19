# Bonsai Watering - Scheduler

## Jobs

### Water plants
```shell
curl http://127.0.0.1:8000/api/v1/job/ -d \
'{
  "epsilon": "PT5S",
  "command": "mqtt_water_plants.sh -t 'bonsai/set/plants/default' -d 5",
  "name": "water_plants",
  "schedule": "R/2021-12-23T10:00:00+02:00/P1D"
}'
```
Useful: `date --iso-8601=seconds`

- `/jobs/mqtt_water_plants.sh`

**Arguments**
`-b` binary location, default `MOSQUITTO_PUB`
`-u` broker username, default `MOSQUITTO_USERNAME`
`-P` broker password, default `MOSQUITTO_PASSWORD`
`-h` broker host, default `MOSQUITTO_HOSTNAME`
`-p` broker port, default `MOSQUITTO_PORT`
`-q` QoS, default `MOSQUITTO_QOS`
`-d` duration, default `10`
`-t` topic

All default values are declared in `kala/.env`

The script will send two messages: 
1) To activate the pump with data `{"pump": 1}`
2) To deactivate the pump with data `{"pump": 0}`
