## Articles

- Consume MQTT
`https://github.com/influxdata/telegraf/tree/release-1.21/plugins/inputs/mqtt_consumer`

- Input data format
`https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_INPUT.md`

- Example project
`https://questdb.io/tutorial/2020/08/25/questitto/`

- Parse MQTT and JSON
`https://www.influxdata.com/blog/mqtt-topic-payload-parsing-telegraf/`

## InfluxDB line protocol

- MQTT Input
```
bonsai/status/common -> {"temp": 20, "humidity": 50, "sunlight": 40, "reservoir_alert": 0, "ts": "1640786943"}

bonsai/status/plants/elk -> {"pump": 0, "sprayer": 0, "moisture": 20, "ts": "1640786943"}
bonsai/status/plants/X -> ...
...

bonsai/status/board -> {"raw_temp": 40, "mem_alloc": 100, "mem_free": 200, "mem_total": 300, "ts":"1640786943"}
```

- Influx LP Output
```
bonsai_common,query=status temp=20i,humidity=50i,sunlight=40i,reservoir_alert=true 1640786943000000000

bonsai_plants,name=elk,query=status pump=false,sprayer=false,moisture=20i 1640786943000000000
bonsai,name=plant-X ...
...

bonsai_board,query=status raw_temp=20i,mem_alloc=200i,mem_free=200i,mem_total=400i 1640786943000000000
```

## Debug Telegraf
```
docker run --rm -v $PWD/telegraf.conf:/etc/telegraf/telegraf.conf:ro telegraf
```
