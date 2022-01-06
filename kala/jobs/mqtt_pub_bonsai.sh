#!/usr/bin/env bash

# Bash options
set -e

# Default values
MQTT_PUB='/usr/bin/mosquitto_pub'
HOST='172.17.0.3'
PORT='8888'
QOS='1'
INTERVAL='10'

usage() {
  cat <<-EOF
-b Binary: path to mosquitto_pub, default $MQTT_PUB
-h Host: MQTT broker hostname, default $HOST
-p Port: MQTT broker port, default $PORT
-q QoS: MQTT quality of service, default $QOS

-t Topic: MQTT topic
-m Message: MQTT payload

-s Sleep interval, default $INTERVAL
EOF
}

while getopts ':b:h:p:q:t:m:s:' opt; do
  case "$opt" in
    b) MQTT_PUB="$OPTARG" ;;
    h) HOST="$OPTARG" ;;
    p) PORT="$OPTARG" ;;
    q) QOS="$OPTARG" ;;
    t) TOPIC="$OPTARG" ;;
    m) MESG="$OPTARG" ;;
    s) INTERVAL="$OPTARG" ;;
  esac
done

readonly MQTT_PUB HOST PORT QOS TOPIC MESG INTERVAL

# mosquitto_pub -h 172.17.0.3 -p 8888 -q 1 -t 'bonsai_watering/set/pump' -m 0

"$MQTT_PUB" -h "$HOST" -p "$PORT" -q "$QOS" -t "$TOPIC" -m "$MESG"
sleep "$INTERVAL"
"$MQTT_PUB" -h "$HOST" -p "$PORT" -q "$QOS" -t "$TOPIC" -m '0'
