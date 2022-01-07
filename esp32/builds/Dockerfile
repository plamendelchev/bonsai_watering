# Global args
ARG PATH="$HOME/.local/bin:$PATH"

# Build stage
FROM centos:latest AS builder

# Set up variables
ENV PATH=$PATH

# install depedencies
RUN dnf update -y && \
	dnf install epel-release -y && \
	dnf install 'dnf-command(config-manager)' -y && \
	dnf config-manager --set-enabled powertools -y && \
	dnf update -y && \
	dnf install gcc gcc-c++ glibc-devel make which git wget flex bison gperf python39 cmake ninja-build ccache libffi libffi-devel -y && \
	dnf clean all

# clone and install esp-idf
ARG ESP_IDF=v4.3.2
RUN mkdir /esp/ && \
  git -C /esp/ clone -b $ESP_IDF --recursive https://github.com/espressif/esp-idf.git && \ 
  git -C /esp/esp-idf submodule update --init && \
  /esp/esp-idf/install.sh esp32

# clone micropython
ARG MICRO_PYTHON=v1.17
RUN git -C /esp/ clone -b $MICRO_PYTHON https://github.com/micropython/micropython

# build micropython cross-compiler
RUN source /esp/esp-idf/export.sh && \ 
  make -j 4 -C /esp/micropython/mpy-cross && \
  cp /esp/micropython/mpy-cross/mpy-cross /usr/bin/ && chmod 744 /usr/bin/mpy-cross

# build micropython-linux port
RUN source /esp/esp-idf/export.sh && \
  cd /esp/micropython/ports/unix && \
  make -j 4 submodules && make -j 4 && make test && \
  cp /esp/micropython/ports/unix/micropython /usr/bin/ && chmod 744 /usr/bin/micropython

# Copy modules into build directory
ADD ./modules /esp/micropython/ports/esp32/modules/

# build firmware
RUN source /esp/esp-idf/export.sh && \
  make -j 4 -C /esp/micropython/ports/esp32 submodules && \
  make -j 4 -C /esp/micropython/ports/esp32
