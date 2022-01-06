#/usr/bin/env bash

# create container 
docker create -it \
  --name spas \
  --mount type=bind,source="$HOME"/bonsai_watering/esp32/src,destination=/esp/bonsai_watering \
  centos8-micropython_v4.3-v1.16:firmware bash &&

# start container 
docker start -ai spas
