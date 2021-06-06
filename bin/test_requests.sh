#!/usr/bin/env bash

test_get="curl -XGET -H 'Content-type: application/json' http://192.168.0.197/pump -s | jq '.'"
printf '%s\n' "-- $test_get"
eval "$test_get"

test_on="curl -d '{\"status\":1}' -H 'Content-type: application/json' http://192.168.0.197/pump -s | jq '.'"
printf '\n%s\n' "-- $test_on"
eval "$test_on"

test_off="curl -d '{\"status\":0}' -H 'Content-type: application/json' http://192.168.0.197/pump -s | jq '.'"
printf '\n%s\n' "-- $test_off"
eval "$test_off"
