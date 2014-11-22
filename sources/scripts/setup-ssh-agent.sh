#!/bin/bash

# set up ssh-agent

eval `ssh-agent -s`
ssh-add /root/.ssh/id_rsa