#!/bin/bash

# ANSI escape code for bright green
GREEN="\e[92m"
RESET="\e[0m"

while true; do
  printf "${GREEN}%s${RESET}\n" "$(echo $RANDOM | md5sum | head -c 30)"
  sleep 0.1
done
