#!/bin/bash

# set up ssh-agent

eval `ssh-agent -s`
ssh-add /root/.ssh/id_rsa

# git clone the latest ansible playbooks

cd /etc/ansible/playbooks
git clone git@github.com:mrkyle7/KY-home-playbooks.git
cd KY-home-playbooks
echo ""
echo "cd $(pwd)"
