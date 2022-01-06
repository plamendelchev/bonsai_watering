# Mosquitto broker

- Create MQTT users from `passwd` file
```
docker run -it --rm -v $PWD/mosquitto/config:/mosquitto/config eclipse-mosquitto mosquitto_passwd -U /mosquitto/config/passwd
```
