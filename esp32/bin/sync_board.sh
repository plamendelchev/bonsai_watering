#!/usr/bin/env bash

PWD="$({ cd "$(dirname ${BASH_SOURCE[0]})"; cd ../ ; } &> /dev/null && pwd)"

rshell rsync src/ /pyboard/
