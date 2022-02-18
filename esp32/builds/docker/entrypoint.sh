#!/usr/bin/env bash

source '/esp/esp-idf/export.sh'
readonly DIR='/esp/micropython/ports/esp32'

make clean -C "$DIR" &&
make submodules -j 4 -C "$DIR" &&
make -j 4 -C "$DIR" &&

mv -v /esp/micropython/ports/esp32/build-GENERIC/firmware.bin /esp
