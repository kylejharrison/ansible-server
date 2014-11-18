#!/bin/sh
docker build -t mrkyle7/ansible-server:stable .
if [ $? -eq 0 ] ; then
    docker push mrkyle7/ansible-server:latest
fi
