#!/bin/bash
#functions
unenv () {
    if [ -f "${SMOKE_ENV_DIR}/.unenv" ] ; then
        source "${SMOKE_ENV_DIR}/.unenv"
        unset SMOKE_ENV_DIR
    else
        false
    fi
}

mkenv () {
    unenv || true
    if [ -f .mkenv ] && [ "${SMOKE_ENV_DIR}x" != "$(pwd)x" ] ; then
        echo "Adding $(pwd) env"
        source .mkenv
        export SMOKE_ENV_DIR="$(pwd)"
    else
        false
    fi
}
