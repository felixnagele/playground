#!/bin/bash

text="Hi, my name is Felix."
delay=0.20  # Seconds between each character

# Hide cursor
echo -ne "\e[?25l"
trap "echo -ne '\e[0m\e[?25h'; exit" INT

for ((i=0; i<${#text}; i++)); do
  printf "%s" "${text:$i:1}"
  sleep "$delay"
done

echo
echo -ne "\e[?25h"
