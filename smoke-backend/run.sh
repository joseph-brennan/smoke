#!/bin/bash
[ -f $HOME/.bashrc ] && source $HOME/.bashrc
source smoke-env
cd $(dirname $0)
mkenv
flask run -h 0.0.0.0 -p 8000
