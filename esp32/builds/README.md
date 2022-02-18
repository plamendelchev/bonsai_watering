# Build and flash MicroPython

**Build container**
- Available build arguments: `ESP_IDF`, `MICRO_PYTHON`
```
docker build -t stream8-micropython:1.17 ./docker
docker build --build-arg ESP_IDF=v4.3.2 -t stream8-micropython:1.17 ./docker
```

**Compile firmware**
`docker run --name mitko -v "$PWD"/modules:/esp/micropython/ports/esp32/modules stream8-micropython:1.17`

**Export firmware**
`docker cp mitko:/esp/firmware.bin ./roms/NAME.bin && docker container rm mitko`

**Reflash firmware**
```
esptool.py erase_flash
esptool.py write_flash -z 0x1000 ./roms/NAME.bin
```
