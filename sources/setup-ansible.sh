#!/bin/bash

#Start ssh agent
eval `ssh-agent -s`
ssh-add /root/.ssh/id_rsa

