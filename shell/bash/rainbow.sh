#!/bin/bash

# Terminal width
cols=$(tput cols 2>/dev/null || echo 80)

# 7 rainbow colors (ANSI 256)
RED=196
ORANGE=208
YELLOW=226
GREEN=46
BLUE=21
INDIGO=93
VIOLET=201

colors=($RED $ORANGE $YELLOW $GREEN $BLUE $INDIGO $VIOLET)

# Amount of columns per color segment
segment=$((cols / 7))

# Build rainbow line
rainbow_line=""
for color in "${colors[@]}"; do
  for ((i=0; i<segment; i++)); do
    rainbow_line+="\e[38;5;${color}m█"
  done
done

# Fill remaining columns if any
rest=$((cols - segment*7))
for ((i=0; i<rest; i++)); do
  rainbow_line+="\e[38;5;${VIOLET}m█"
done

reset="\e[0m"

# Scrolling rainbow
while true; do
  echo -e "${rainbow_line}${reset}"
  sleep 0.02
done
