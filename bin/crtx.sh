#!/bin/bash

# NB: execute crtx.sh using ./crtx.sh
# Do not use space, IFS is the default behaviour

if [ -z "$1" ]; then
    echo "Please provide a project name after ./crtx.sh"
    echo "Exit script without create any directories or files"
    exit 1
fi

current_path=$(pwd)
folder_path="./../Exercises"
# project_name="$1"
directories=$(find "$folder_path" -maxdepth 1 -type d)
num_directories=$(find "$folder_path" -maxdepth 1 -type d | wc -l )

echo "😂:$directories"
echo "$num_directories"
echo "🤣:$current_path"
echo "$0"
dirname "$0"
for dir in "$directories"; do echo "🤑$dir"; done