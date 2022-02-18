#!/bin/sh

# Default vars
DURATION='10'

# ENV vars
# MOSQUITTO_PUB MOSQUITTO_USERNAME MOSQUITTO_PASSWORD MOSQUITTO_HOSTNAME MOSQUITTO_PORT MOSQUITTO_QOS

while getopts ':b:h:p:q:t:d:' opt; do
  case "$opt" in
    # binary
    b) MOSQUITTO_PUB="$OPTARG" ;;
    # username
    u) MOSQUITTO_USERNAME="$OPTARG" ;;
    # password
    P) MOSQUITTO_PASSWORD="$OPTARG" ;;
    # host
    h) MOSQUITTO_HOSTNAME="$OPTARG" ;;
    # port
    p) MOSQUITTO_PORT="$OPTARG" ;;
    # qos
    q) MOSQUITTO_QOS="$OPTARG" ;;
    # topic
    t) TOPIC="$OPTARG" ;;
    # duration
    d) DURATION="$OPTARG" ;;
  esac
done

readonly MOSQUITTO_PUB MOSQUITTO_USERNAME MOSQUITTO_PASSWORD MOSQUITTO_HOSTNAME MOSQUITTO_PORT MOSQUITTO_QOS TOPIC DURATION

# mosquitto_pub -h 172.17.0.3 -p 8888 -q 1 -t 'bonsai_watering/set/plants/default' -m '{"pump": 1}'

"$MOSQUITTO_PUB" -u "$MOSQUITTO_USERNAME" -P "$MOSQUITTO_PASSWORD" -h "$MOSQUITTO_HOSTNAME" -p "$MOSQUITTO_PORT" -q "$MOSQUITTO_QOS" -t "$TOPIC" -m '{"pump": 1}'

sleep "$DURATION"

"$MOSQUITTO_PUB" -u "$MOSQUITTO_USERNAME" -P "$MOSQUITTO_PASSWORD" -h "$MOSQUITTO_HOSTNAME" -p "$MOSQUITTO_PORT" -q "$MOSQUITTO_QOS" -t "$TOPIC" -m '{"pump": 0}'
