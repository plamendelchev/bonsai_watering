FROM eclipse-mosquitto:latest

COPY ./config /mosquitto/config

RUN mosquitto_passwd -U /mosquitto/config/passwd
