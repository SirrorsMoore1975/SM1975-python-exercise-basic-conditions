#!/bin/bash

# NB: execute crtx.sh using ./crtx.sh
# Do not use space, IFS is the default behaviour

if [ -z "$1" ]; then
    echo "Please provide a project name after ./crtx.sh"
    echo "Exit script without create any directories or files"
    exit 1
fi

project_name="$1"

