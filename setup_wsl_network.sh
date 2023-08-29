#!/bin/bash

ADDRESS="192.168.200.232/24"
DEV="eth0"

if [[ "$1" == "-d" ]]; then
  echo "Removing IP address $ADDRESS on $DEV"
  ip address del $ADDRESS dev $DEV
else
  echo "Adding IP address $ADDRESS on $DEV"
  ip address add $ADDRESS dev $DEV
fi
