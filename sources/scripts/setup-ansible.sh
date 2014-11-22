#!/bin/bash

# git clone the latest ansible playbooks

cd /etc/ansible/playbooks
git clone git@github.com:mrkyle7/home-playbooks.git
cd home-playbooks
echo ""
echo "cd $(pwd)"
