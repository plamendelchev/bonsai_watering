#!/usr/bin/env bash

source GLOBALS # Introduces $VERSION $PACKAGES

# Build base image
docker build -t centos8-micropython_"$VERSION":base -f ./docker-files/base.Dockerfile .
