#!/bin/bash

echo -ne "\e[?25l"
trap "echo -ne '\e[0m\e[?25h'; exit" INT

spinner='|/-\'
bar_width=40

# Simulate progress
for ((i=0; i<=100; i++)); do
  spin=${spinner:i%4:1}
  filled=$(( i * bar_width / 100 ))

  # Build progress bar string
  bar=""
  for ((j=0; j<filled; j++)); do bar+="#"; done
  for ((j=filled; j<bar_width; j++)); do bar+="."; done

  # Display progress bar
  printf "\r[%s] %3d%% %s" "$bar" "$i" "$spin"
  sleep 0.05
done

echo -e "\nFinished!"
echo -ne "\e[?25h"
