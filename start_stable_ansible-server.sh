#!/bin/sh

docker pull mrkyle7/ansible-server:stable
docker run -it mrkyle7/ansible-server:stable /bin/bash
