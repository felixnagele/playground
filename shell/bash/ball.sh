#!/bin/bash

frames=(
"   O   \n       \n       "
"       \n   O   \n       "
"       \n       \n   O   "
"       \n   O   \n       "
)

while true; do
  for f in "${frames[@]}"; do
    printf "\e[2J\e[H"   # clear + cursor home
    printf "%b" "$f"
    sleep 0.1
  done
done
