#!/bin/sh

export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
ansible-playbook ansible/site.yaml "$@"
