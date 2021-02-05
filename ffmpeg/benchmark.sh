#!/bin/bash

f=sample.mp4

if [ ! -z "$1" ]; then
    f=$1
fi

if [ ! -f $f ]; then
    echo "file not found: $f"
    exit
fi

TIMEFORMAT=%R; time ffmpeg -hide_banner -loglevel error -i $f -benchmark -f null -
