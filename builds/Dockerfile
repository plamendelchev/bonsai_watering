FROM centos8-micropython:base

# build cross-compiler
RUN cd /esp/micropython && make -C mpy-cross

# freeze module
RUN mkdir /esp/micropython/ports/esp32/modules/MicroWebSrv2/
COPY ./packages/MicroWebSrv2/MicroWebSrv2/ /esp/micropython/ports/esp32/modules/MicroWebSrv2/

RUN mkdir /esp/micropython/ports/esp32/modules/schedule/
COPY ./packages/schedule/schedule/schedule.py /esp/micropython/ports/esp32/modules/

# build micropython
RUN export PATH="$PATH:/root/.local/bin/" && source /esp/esp-idf/export.sh && cd /esp/micropython/ports/esp32 && make submodules && make

# remove unnecessary stuff
RUN cd /esp/micropython/ports/esp32/modules/ && rm -f apa106.py neopixel.py
