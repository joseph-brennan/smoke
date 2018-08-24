#!/bin/bash
bash smoke-scripts/scripts/bootstrap.sh
mkdir -p "${HOME}/.local/bin"
cp smoke-scripts/scripts/env.sh ${HOME}/.local/bin/smoke-env
chmod +x ${HOME}/.local/bin/smoke-env
export PATH="${PATH}:${HOME}/.local/bin"
source smoke-env

for part in smoke-editor smoke-backend smokr; do
    pushd ${part}
    [ -f .travis/install.sh ] && bash .travis/install.sh
    popd
done
