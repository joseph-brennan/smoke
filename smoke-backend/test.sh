#!/bin/bash

[ -f $HOME/.bashrc ] && source $HOME/.bashrc
SMOKE_ENV=$(which smoke-env)
SMOKE_ENV=${SMOKE_ENV:-../smoke-scripts/scripts/smoke-env}

if [ -f ${SMOKE_ENV} ] ; then
  cd $(dirname $0)
  source ${SMOKE_ENV}
  mkenv
  tox
else
  echo "smoke-env not found."
  exit 1
fi

