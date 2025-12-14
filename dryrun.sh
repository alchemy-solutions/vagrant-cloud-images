#!/bin/sh

export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES

hcp auth login

ansible-playbook -e dryrun=True ansible/site.yaml "$@"
