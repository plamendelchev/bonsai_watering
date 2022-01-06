# Mosquitto broker

- Create MQTT users from `passwd` file
```
cp passwd config/
docker run -it --rm -v $PWD/config:/mosquitto/config eclipse-mosquitto mosquitto_passwd -U /mosquitto/config/passwd
```
