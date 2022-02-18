## Build firmware

- Info `https://docs.docker.com/develop/develop-images/multistage-build/`
```
docker build -t centos8-micropython:1.17 .
docker build --build-arg ESP_IDF=v4.3.2 builder -t centos8-micropython:1.17 .
```

## Export firmware

```
docker create --name mitko centos8-micropython:1.17
docker cp mitko:/esp/micropython/ports/esp32/build-GENERIC/firmware.bin ./roms/NAME.bin
docker container rm mitko
```

## Flash firmware
```
esptool.py erase_flash
esptool.py write_flash -z 0x1000 ./roms/NAME.bin
```
