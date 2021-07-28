#!/usr/bin/env bash

VERSION='v4.3-v1.16'
PACKAGES='mws2'

docker build -t centos8-micropython_base:"$VERSION" -f Dockerfile_base . &&

docker build -t centos8-micropython:"$VERSION" -f Dockerfile . &&

docker create --name mitko centos8-micropython:"$VERSION" &&
docker cp mitko:/esp/micropython/ports/esp32/build-GENERIC/firmware.bin ./firmwares/esp32_"$VERSION"_"$PACKAGES".bin


