#!/bin/sh
cd ./atomic-host-tests/
export ANSIBLE_HOST_KEY_CHECKING=False
ansible-playbook -i inventory tests/improved-sanity-test/main.yml
