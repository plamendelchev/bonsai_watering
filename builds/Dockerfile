FROM centos8-micropython:base

# set up env vars
#RUN export PATH="$PATH:/root/.local/bin/" && source /esp/esp-idf/export.sh

# build cross-compiler
RUN cd /esp/micropython && make -C mpy-cross

# freeze module
RUN mkdir /esp/micropython/ports/esp32/modules/MicroWebSrv2/
COPY MicroWebSrv2/MicroWebSrv2/ /esp/micropython/ports/esp32/modules/MicroWebSrv2/

# set up env vars
#RUN source /esp/esp-idf/export.sh

# build micropython
RUN export PATH="$PATH:/root/.local/bin/" && source /esp/esp-idf/export.sh && cd /esp/micropython/ports/esp32 && make submodules && make
