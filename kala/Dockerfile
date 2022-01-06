# Build kala
FROM golang:latest AS build

WORKDIR /go/src/github.com/ajvb/kala
COPY ./kala .

RUN CGO_ENABLED=0 go build

# Run kala
FROM alpine:latest AS run

EXPOSE 8000
ENV PATH="/jobs:$PATH"

COPY --from=build /go/src/github.com/ajvb/kala/kala /usr/local/bin
COPY ./jobs /jobs

RUN apk --no-cache add mosquitto-clients && mkdir /kala

CMD ["kala", "serve", "--jobdb=boltdb", "--bolt-path=/kala"]
