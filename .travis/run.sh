#!/bin/bash
# make sure failing tests cause failing
export PATH="${PATH}:${HOME}/.local/bin"
pushd $(dirname $0)/..
for part in smoke-editor smoke-backend smokr; do
    pushd ${part}
    set -e
    [ -f .travis/test.sh ] && .travis/test.sh
    set +e
    popd
done
popd
