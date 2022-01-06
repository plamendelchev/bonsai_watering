FROM centos8-micropython_v4.3-v1.16:base

# Copy modules into build directory
ADD ./modules /esp/micropython/ports/esp32/modules/

# build firmware
RUN rm -f /esp/micropython/ports/esp32/modules/{apa106.py,neopixel.py} ; \
  source /esp/esp-idf/export.sh && \ 
  make -C /esp/micropython/ports/esp32 submodules && \ 
  make -C /esp/micropython/ports/esp32
