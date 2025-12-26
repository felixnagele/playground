#!/bin/bash

text="SHELL"
colors=(196 208 226 46 21 93 201)

# Hide cursor
echo -ne "\e[?25l"

trap "echo -ne '\e[0m\e[?25h'; exit" INT

while true; do
  for c in "${colors[@]}"; do
    # Set cursor to beginning of line ...
    echo -ne "\r\e[38;5;${c}m\e[5m$text\e[0m"
    sleep 0.15
  done
done
