#!/bin/bash

echo -n "Enter URL: " 
read url

docker run -d \
    --name=firefox \
    -p 5800:5800 \
    -v /c/Users/Kesavasai\ Virinchi/Projects/SecureShield:/config:rw \
    --shm-size 2g \
    -e FF_OPEN_URL="$url" \
    jlesage/firefox

echo -n "Would you like to terminate?"
read terminate

if [[ "$terminate" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    docker kill firefox
fi