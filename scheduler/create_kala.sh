#!/usr/bin/env bash

docker run -it -d \
  -p 8000:8000 \
  --name kala \
  --mount type=bind,source="$PWD"/jobs,target=/jobs \
  kala
