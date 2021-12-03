#!/usr/bin/env bash

source ~/argo_mail/venv/bin/activate

cd ~/argo_mail && python3 main.py

deactivate

#tail -f /Users/kellyfoulk/Documents/code/Argo_mail/cronlog.txt
