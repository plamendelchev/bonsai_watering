#!/usr/bin/env bash

source GLOBALS # Introduces $VERSION $PACKAGES

# Build firmware
docker build -t centos8-micropython_"$VERSION":firmware -f ./docker-files/Dockerfile_firmware . &&

# Start container
docker create --name mitko centos8-micropython_"$VERSION":firmware &&

# Export firmware
docker cp mitko:/esp/micropython/ports/esp32/build-GENERIC/firmware.bin ./roms/esp32_"$VERSION"_"$PACKAGES".bin

# Delete container
docker container rm mitko
