# Bonsai Watering - Scheduler

## Jobs

### Water plants
```shell
curl http://127.0.0.1:8000/api/v1/job/ -d \
'{
  "epsilon": "PT5S",
  "command": "mqtt_pub_bonsai.sh -t 'bonsai_watering/set/pump' -m 1 -s 5",
  "name": "water_bonsai",
  "schedule": "R/2021-12-23T10:00:00+02:00/PT1D"
}'
```
Useful `date --iso-8601=seconds`
