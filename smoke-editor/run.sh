#!/bin/bash
[ -f $HOME/.bashrc ] && source $HOME/.bashrc
source smoke-env
cd $(dirname $0)
mkenv
HOST=0.0.0.0 yarn dev
