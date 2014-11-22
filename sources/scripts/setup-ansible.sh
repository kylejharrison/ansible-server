#!/bin/bash

# git clone the latest ansible playbooks

cd /etc/ansible/playbooks
git clone git@github.com:mrkyle7/KY-home-playbooks.git
cd KY-home-playbooks
echo ""
echo "cd $(pwd)"
