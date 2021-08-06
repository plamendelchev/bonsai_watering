FROM centos:latest

# Set up env variables
RUN sed -i '/^PATH/s/$/:$HOME\/.local\/bin/' $HOME/.bash_profile && source $HOME/.bash_profile

# install depedencies
RUN dnf update -y && \
	dnf install epel-release -y && \
	dnf install 'dnf-command(config-manager)' -y && \
	dnf config-manager --set-enabled powertools -y && \
	dnf update -y && \
	dnf install gcc gcc-c++ glibc-devel make which git wget flex bison gperf python39 cmake ninja-build ccache libffi libffi-devel -y && \
	dnf clean all

# clone and install esp-idf
RUN mkdir /esp/ && \
  git -C /esp/ clone -b v4.3 --recursive https://github.com/espressif/esp-idf.git && \ 
  git -C /esp/esp-idf/ checkout v4.3 && \
  git -C /esp/esp-idf submodule update --init \ 
    components/bt/host/nimble/nimble \ 
    components/esp_wifi \ 
    components/esptool_py/esptool \
    components/lwip/lwip \ 
    components/mbedtls/mbedtls \
    components/bt/controller/lib_esp32 \
    components/bt/controller/lib_esp32c3_family && \
  /esp/esp-idf/install.sh

# clone micropython
RUN source /esp/esp-idf/export.sh && \
  git -C /esp/ clone -b v1.16 https://github.com/micropython/micropython && \ 
  git -C /esp/micropython/ checkout v1.16

# clone webrepl
RUN git -C /esp/ clone https://github.com/micropython/webrepl

# build micropython cross-compiler
RUN source /esp/esp-idf/export.sh && \ 
  make -C /esp/micropython/mpy-cross && \
  cp /esp/micropython/mpy-cross/mpy-cross /usr/bin/ && chmod 744 /usr/bin/mpy-cross

# build micropython-linux port
RUN source /esp/esp-idf/export.sh && \
  cd /esp/micropython/ports/unix && \
  make submodules && make && make test && \
  cp /esp/micropython/ports/unix/micropython /usr/bin/ && chmod 744 /usr/bin/micropython

