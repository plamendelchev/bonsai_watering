#!/bin/sh

# Default vars
INTERVAL='10'

# ENV vars
# MOSQUITTO_PUB MOSQUITTO_USERNAME MOSQUITTO_PASSWORD MOSQUITTO_HOSTNAME MOSQUITTO_PORT MOSQUITTO_QOS

while getopts ':b:h:p:q:t:m:s:' opt; do
  case "$opt" in
    # binary
    b) MOSQUITTO_PUB="$OPTARG" ;;
    # username
    u) MOSQUITTO_USERNAME="$OPTARG" ;;
    # password
    u) MOSQUITTO_PASSWORD="$OPTARG" ;;
    # host
    h) MOSQUITTO_HOSTNAME="$OPTARG" ;;
    # port
    p) MOSQUITTO_PORT="$OPTARG" ;;
    # qos
    q) MOSQUITTO_QOS="$OPTARG" ;;
    # topic
    t) TOPIC="$OPTARG" ;;
    # message
    m) MESG="$OPTARG" ;;
    # seconds
    s) INTERVAL="$OPTARG" ;;
  esac
done

readonly MOSQUITTO_PUB MOSQUITTO_USERNAME MOSQUITTO_PASSWORD MOSQUITTO_HOSTNAME MOSQUITTO_PORT MOSQUITTO_QOS TOPIC MESG INTERVAL

# mosquitto_pub -h 172.17.0.3 -p 8888 -q 1 -t 'bonsai_watering/set/pump' -m 0

"$MOSQUITTO_PUB" -u "$MOSQUITTO_USERNAME" -P "$MOSQUITTO_PASSWORD" -h "$MOSQUITTO_HOSTNAME" -p "$MOSQUITTO_PORT" -q "$MOSQUITTO_QOS" -t "$TOPIC" -m "$MESG"

sleep "$INTERVAL"

"$MOSQUITTO_PUB" -u "$MOSQUITTO_USERNAME" -P "$MOSQUITTO_PASSWORD" -h "$MOSQUITTO_HOSTNAME" -p "$MOSQUITTO_PORT" -q "$MOSQUITTO_QOS" -t "$TOPIC" -m '0'
