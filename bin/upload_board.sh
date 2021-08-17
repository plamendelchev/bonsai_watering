#!/usr/bin/env bash

readonly IP='192.168.0.197'

printf '\n%s %s\n\n' '-- Shutting down server -' "$(curl -s -XGET -H 'Content-type: application/json' http://"$IP"/webrepl)"

sleep 3

git diff --name-only $(git log | grep -m2 -Po '(?<=commit )[\d\w]+' | grep 'esp32') | xargs realpath | while read -r file; do
  webrepl_cli.py -p 'gosho123' "$file" "$IP":"${file//'/home/esp32/bonsai_watering/esp32'}"
done
