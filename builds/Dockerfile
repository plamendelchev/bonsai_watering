FROM centos8-micropython_base:v4.3-v1.16

# freeze modules
RUN mkdir /esp/micropython/ports/esp32/modules/MicroWebSrv2/
COPY ./packages/MicroWebSrv2/MicroWebSrv2/ /esp/micropython/ports/esp32/modules/MicroWebSrv2/

# remove unnecessary stuff
RUN rm -f /esp/micropython/ports/esp32/modules/{apa106.py,neopixel.py}

# build micropython
RUN export PATH="$PATH:/root/.local/bin/" && source /esp/esp-idf/export.sh && \ 
  cd /esp/micropython/ports/esp32 && \ 
  make submodules && make
