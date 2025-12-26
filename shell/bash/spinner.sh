#!/bin/bash

chars='/-\|'

# Hide cursor
echo -ne "\e[?25l"

# Ensure cursor is shown again on exit
trap "echo -ne '\e[0m\e[?25h'; exit" INT

i=0
while true; do
  printf "\r%s" "${chars:i%4:1}"
  i=$((i + 1))
  sleep 0.1
done
