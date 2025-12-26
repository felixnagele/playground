#!/bin/bash

chars='/-\|'

# Hide cursor
echo -ne "\e[?25l"

# Ensure cursor is shown again on exit
trap "echo -ne '\e[0m\e[?25h'; exit" INT

while true; do
  for i in {1..50}; do
    printf "\r%s" "${chars:i%4:1}"
    sleep 0.1
  done
done
