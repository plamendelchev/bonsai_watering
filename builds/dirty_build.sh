#!/usr/bin/env bash

## Build firmware
docker build -t 'centos8-micropython:firmware' -f Dockerfile .

## Export firmware
docker create --name mitko 'centos8-micropython:firmware'
docker cp mitko:/esp/micropython/ports/esp32/build-GENERIC/firmware.bin ./firmwares/
