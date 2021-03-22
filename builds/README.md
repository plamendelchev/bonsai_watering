# Build micropython with frozen modules
---

## Usage

1. Build base image
```shell
docker build -t centos8-micropython:base -f Dockerfile_base .
```

2. Build main image
```shell
docker build -t centos8-micropython -f Dockerfile .
```

3. Export built image
```shell
docker create --name mitko centos8-micropython:1.1
docker cp mitko:/esp/micropython/ports/esp32/build-GENERIC/bootloader/firmware.bin .
```
